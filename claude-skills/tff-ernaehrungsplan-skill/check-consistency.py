#!/usr/bin/env python3
"""Consistency checks for the TFF Nutrition Plan Skill.

Run from anywhere:  python3 check-consistency.py
Each check guards a rule the skill depends on: every number has a source,
the same range says the same thing in every file, safety comes before the
modes, and the disclaimer keeps all of its clauses.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent


def read(rel):
    return (HERE / rel).read_text(encoding="utf-8")


SKILL = read("SKILL.md")
SOURCES = read("reference/sources.md")
CLAIMS = read("reference/claims.md")
SUPPS = read("reference/supplements.md")
FAT = read("goals/fat-loss.md")
GAIN = read("goals/muscle-gain.md")
ENDU = read("goals/endurance.md")
AGE = read("modifiers/age.md")
SPORT = read("modifiers/sport.md")
ASSESS_RAW = read("assessment.json")

MD_FILES = {
    "SKILL.md": SKILL,
    "reference/claims.md": CLAIMS,
    "reference/supplements.md": SUPPS,
    "goals/fat-loss.md": FAT,
    "goals/muscle-gain.md": GAIN,
    "goals/endurance.md": ENDU,
    "modifiers/age.md": AGE,
    "modifiers/sport.md": SPORT,
}

results = []


def check(name, condition, detail=""):
    results.append((name, bool(condition), detail))


def norm(text):
    """Unify dashes and thin spaces so '1.6–2.2' and '1.6-2.2' compare equal."""
    return text.replace("–", "-").replace("−", "-").replace(" ", " ")


# --- structure ----------------------------------------------------------------
try:
    assess = json.loads(ASSESS_RAW)
    check("assessment.json parses", True)
except json.JSONDecodeError as exc:
    assess = {}
    check("assessment.json parses", False, str(exc))

check("SKILL.md frontmatter has name + description",
      re.search(r"^name:\s*\S+", SKILL, re.M) and re.search(r"^description:\s*\S+", SKILL, re.M))
versions = re.findall(r"^version:\s*(\S+)", SKILL, re.M)
check("SKILL.md declares exactly one version", len(versions) == 1, str(versions))

for rel, text in MD_FILES.items():
    if rel == "SKILL.md":
        continue
    body = text.split("---", 2)[-1]
    check(f"{rel}: H1 sits outside the frontmatter", body.lstrip().startswith("#"))

for ref in sorted(set(re.findall(r"`((?:goals|modifiers|reference)/[\w-]+\.md)`", SKILL))):
    check(f"SKILL.md references existing file {ref}", (HERE / ref).exists())

rules = [int(n) for n in re.findall(r"^(\d+)\. (?:⚠️ )?\*\*", SKILL.split("## MANDATORY RULES")[1].split("\n---")[0], re.M)]
check("MANDATORY RULES numbered 1..N without gaps", rules == list(range(1, len(rules) + 1)), str(rules))

# --- safety order ---------------------------------------------------------------
def pos(heading):
    m = re.search(rf"^## {re.escape(heading)}", SKILL, re.M)
    return m.start() if m else -1


triage = pos("SAFETY TRIAGE")
check("SAFETY TRIAGE section exists", triage > 0)
for mode in ("HARD FLOORS", "NEW PLAN MODE", "UPDATE MODE", "ANALYSIS MODE"):
    check(f"SAFETY TRIAGE comes before {mode}", 0 < triage < pos(mode))
for mode in ("UPDATE MODE", "ANALYSIS MODE"):
    section = SKILL[pos(mode):]
    section = section[: section.find("\n## ", 5)]
    check(f"{mode} runs the triage", "SAFETY TRIAGE" in section)

for signal in ("eating disorder", "18.5", "Pregnancy", "Under 18", "insulin", "kidney", "GLP-1", "coeliac", "RED-S"):
    check(f"triage covers: {signal}", signal in SKILL[triage:pos("HARD FLOORS")])

# --- disclaimer -----------------------------------------------------------------
disc = SKILL[pos("DISCLAIMER"):]
en = disc.split("**English:**")[1].split("**German:**")[0]
de = disc.split("**German:**")[1]
for clause in ("not medical advice", "position stands", "pregnant or breastfeeding", "under 18",
               "eating disorder", "not a substitute", "pharmacist", "own risk"):
    check(f"EN disclaimer keeps: {clause}", clause in en)
for clause in ("keine ärztliche Beratung", "Positionspapieren", "schwanger bist oder stillst", "unter 18",
               "Essstörung", "ersetzen keine", "Apotheke", "eigene Verantwortung"):
    check(f"DE disclaimer keeps: {clause}", clause in de)

# --- source register ------------------------------------------------------------
q_defined = set(re.findall(r"^\| (Q\d+) \|", SOURCES, re.M))
h_defined = set(re.findall(r"^\| (H\d+) \|", SOURCES, re.M))
check("source register defines Q-codes contiguously",
      q_defined == {f"Q{i}" for i in range(1, len(q_defined) + 1)}, str(sorted(q_defined, key=lambda c: int(c[1:]))))
check("no Q-row still waits for a status", "see status" not in SOURCES)

all_text = "\n".join(MD_FILES.values()) + ASSESS_RAW
for code in sorted(set(re.findall(r"\b(Q\d+)\b", all_text)), key=lambda c: int(c[1:])):
    check(f"cited {code} exists in the register", code in q_defined)
for code in sorted(set(re.findall(r"\b(H\d+)\b", all_text))):
    check(f"cited {code} exists in the register", code in h_defined)
for code in sorted(q_defined | h_defined, key=lambda c: (c[0], int(c[1:]))):
    check(f"register code {code} is used somewhere", re.search(rf"\b{code}\b", all_text) is not None)

# Q-table must not be split by a blank line (a split table renders as two tables
# and the second half loses its header).
q_block = SOURCES.split("## Q — published sources")[1].split("## H")[0].strip().splitlines()
check("Q table is one contiguous block", all(line.startswith("|") for line in q_block))

# --- every number carries a source ---------------------------------------------
UNIT = re.compile(r"\d[\d.,]*\s*(?:–\s*\d[\d.,]*\s*)?(?:g/kg|kcal|mg|µg|g/h|ml/kg|L/h|mmol|%|g/day|g per)")
CODE = re.compile(r"\b[QH]\d+\b")
for rel in ("goals/fat-loss.md", "goals/muscle-gain.md", "goals/endurance.md",
            "modifiers/age.md", "modifiers/sport.md", "reference/supplements.md"):
    heading_code = False
    unsourced = []
    for line in MD_FILES[rel].splitlines():
        if line.startswith("#"):
            heading_code = bool(CODE.search(line))
            continue
        if not line.startswith("|") or set(line) <= set("|- "):
            continue
        if UNIT.search(line) and not CODE.search(line) and not heading_code:
            unsourced.append(line[:70])
    check(f"{rel}: every table row with a number has a source code", not unsourced, "; ".join(unsourced[:3]))


def walk(node, inherited, path, out):
    if isinstance(node, dict):
        has = inherited or "_source" in node
        if any(k in node for k in ("range", "value", "pal", "pal_add")) and not has:
            out.append(path)
        for k, v in node.items():
            walk(v, has, f"{path}.{k}", out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, inherited, f"{path}[{i}]", out)


missing = []
walk(assess, False, "$", missing)
check("assessment.json: every value block has a _source", not missing, ", ".join(missing[:5]))

# --- same numbers everywhere ----------------------------------------------------
pg = assess.get("protein_g_per_kg", {})
for key, text, label in (
    ("fat_loss_no_strength_training", FAT, "fat-loss.md"),
    ("fat_loss_with_strength_training", FAT, "fat-loss.md"),
    ("fat_loss_lean_trained_sustained_deficit", FAT, "fat-loss.md"),
    ("muscle_gain_training", GAIN, "muscle-gain.md"),
    ("muscle_gain_with_strength_training", GAIN, "muscle-gain.md"),
    ("muscle_gain_default", GAIN, "muscle-gain.md"),
    ("endurance_athletes", ENDU, "endurance.md"),
    ("age_65_plus_minimum", AGE, "age.md"),
):
    rng = pg.get(key, {}).get("range", "<missing>")
    check(f"protein {key} ({rng}) appears in {label}", norm(rng) in norm(text))

carbs = assess.get("carbohydrate_g_per_kg_per_day", {})
for key in ("light", "moderate_about_1h", "high_1_to_3h", "very_high_over_4_to_5h"):
    check(f"carbohydrate {key} matches endurance.md", norm(carbs.get(key, "<missing>")) + " g/kg" in norm(ENDU))

for label, text in (("fat-loss.md", FAT), ("muscle-gain.md", GAIN), ("endurance.md", ENDU)):
    check(f"{label}: fat floor 20 % / range 20-35 %", "20 %" in text and "20-35 %" in norm(text))

floors = assess.get("hard_floors", {})
check("hard floor 1,200 kcal in SKILL.md and assessment.json",
      floors.get("energy_absolute_minimum_kcal", {}).get("value") == 1200 and "1,200 kcal" in SKILL)
check("hard floor 1 %/week in SKILL.md and assessment.json",
      floors.get("max_weight_loss_percent_per_week", {}).get("value") == 1.0 and "at most 1 % of body weight per week" in SKILL)
check("hard floor 24 h fasting in SKILL.md and assessment.json",
      floors.get("max_fasting_hours", {}).get("value") == 24 and "longer than 24 h" in SKILL)
check("H1 300-500 kcal consistent", "300-500" in norm(FAT) and "300-500" in norm(SOURCES))
check("H2 200-300 kcal consistent", "200-300" in norm(GAIN) and "200-300" in norm(SOURCES))

# --- worked examples: arithmetic ------------------------------------------------
MIFFLIN = re.compile(r"10×([\d.]+) \+ 6\.25×([\d.]+) − 5×(\d+) ([+−]) (\d+) = ([\d,.]+)")
for ex in assess.get("examples", []):
    m = MIFFLIN.search(ex.get("resting_energy", ""))
    if not m:
        continue
    w, h, a, sign, c, stated = m.groups()
    value = 10 * float(w) + 6.25 * float(h) - 5 * int(a) + (int(c) if sign == "+" else -int(c))
    check(f"example Mifflin arithmetic ({ex['case'][:30]}…)",
          abs(value - float(stated.replace(",", ""))) < 0.6, f"{value} vs {stated}")

# --- claims ---------------------------------------------------------------------
check("claims.md: German wording filled in (no pending marker)", "DE-WORDING" not in CLAIMS and "pending" not in CLAIMS)
for nutrient in ("Proteine tragen", "Kreatin erhöht", "über 55 Jahre", "Kohlenhydrate tragen",
                 "Kohlenhydrat-Elektrolyt-Lösungen", "Vitamin D trägt"):
    check(f"claims.md has official German wording: {nutrient}", nutrient in CLAIMS)

BANNED = re.compile(r"\b(heilt|beugt\w* vor|Wundermittel|garantiert|entgiftet|verbrennt Fett)\b", re.I)
NEGATION = re.compile(r"\b(no|not|never|nie|kein\w*|nicht|banned|weder|instead|statt)\b|„|\"", re.I)
for rel in ("goals/fat-loss.md", "goals/muscle-gain.md", "goals/endurance.md",
            "modifiers/age.md", "modifiers/sport.md", "reference/supplements.md"):
    hits = [ln.strip()[:60] for ln in MD_FILES[rel].splitlines() if BANNED.search(ln) and not NEGATION.search(ln)]
    check(f"{rel}: no banned effect words outside a rejection", not hits, "; ".join(hits))

check("no brand / shop / affiliate wording in supplements.md",
      not re.search(r"(rabattcode|discount code|affiliate|amazon|\bshop\b(?! or)|®|™)", SUPPS, re.I))

# --- supplement rules -----------------------------------------------------------
check("vegan B12 notice is mandatory in SKILL.md and supplements.md",
      "B12" in SKILL and "mandatory" in SUPPS.lower() and "müssen Personen, die sich vegan ernähren" in SUPPS)
check("iron is never suggested without a lab value", "Never on suspicion" in SUPPS and "Ferritin" in SUPPS)
check("vitamin D upper limit 100 µg cited with Q13", re.search(r"100 µg/day.*Q13", SUPPS) is not None)
check("Rule 16 funding wording present", "funding not checked" in SKILL and "Finanzierung nicht geprüft" in SUPPS)

# --- rules added after validation stage 1 (v0.1.1) ------------------------------
check("claims.md: German protein claim only in official wording", "Protein trägt" not in CLAIMS)
check("energy floor is the higher value, never the sum", "higher of the two values" in SKILL)
check("no time-to-goal estimates (SKILL.md + fat-loss.md)", "No time-to-goal" in SKILL and "Never convert it into a time" in FAT)
check("Rule 3 covers numbers calculated during the assessment", "calculate nothing aloud" in SKILL)
check("H3 default of 5 weeks consistent", all("5 weeks" in t for t in (SOURCES, ENDU, FAT))
      and assess.get("hard_floors", {}).get("no_deficit_days_before_key_race", {}).get("deficit_free_weeks_if_peak_block_unknown") == 5)
check("sport.md forbids interpolating a PAL addition", "do not interpolate" in SPORT)
check("N rules for food values exist and SKILL.md points to them", "## N —" in SOURCES and "N rules" in SKILL)
check("Tier C never used as a verdict on a single ingredient", "never** used as a verdict on a single ingredient" in SUPPS)

check("Rule 17: 5 % applies to all four values", "each of the four values" in SKILL)
check("muscle-gain.md: no safety claim attached to Q3", "not harmful" not in GAIN)

check("RED-S hold row mentions possible pregnancy", "can also mean pregnancy" in SKILL)
check("RED-S hold overrides the one-step rule in UPDATE MODE", "overrides the one-step rule" in SKILL)
check("PAL range is exactly one DGE band", "exactly one DGE band" in SKILL)
check("endurance.md checks fat share per day type", "Check fat per day type" in ENDU)
check("claims.md: every condition kept", "keep **every** condition" in CLAIMS)

# v0.1.4 — findings from the Codex blind test
check("Plan step 3 writes out the floor check", "Floor check, written out" in SKILL)
check("Mifflin intermediate products are shown", "every intermediate product" in SKILL)
check("sport.md: 1-3 sessions use the full band, start in upper half", "full occupation band" in SPORT and "upper half" in SPORT)
check("Pregnancy: own guess after missed period does not rule it out", "the user's own guess after a missed period does not" in SKILL)
check("UPDATE MODE has a minimum output", "Minimum output of every update" in SKILL)
check("Knowledge templates are binding (scales kept)", "the 1–5 scales" in SKILL and "Hunger 1–5 | Energie 1–5" in SKILL)
check("Rule 17: kcal per food from 4/4/9", "kcal per food = 4/4/9" in SKILL)
check("Example days must differ", "never repeat a day under a new name" in SKILL)
check("Under 18: German sentence names the parents", "Bitte sprich mit deinen Eltern" in SKILL)
check("Hold: no deficit without a number, not 'as much as before'", "Iss mehr als in der Abnehmphase" in SKILL and "at least as much as before" not in SKILL)
check("UPDATE: hold signals asked first, without a number", "asks about them and contains no number" in SKILL)
check("UPDATE: current-plan.md replaced as a complete file", "as a complete file that replaces the old one" in SKILL)
check("UPDATE: hold still ends with the minimum output", "the update still ends with the minimum output of step 8" in SKILL and "stop there" not in SKILL)
check("UPDATE: pending energy line in current-plan.md", "neue Zahl erst nach ärztlicher Abklärung" in SKILL)
check("DE no-plan disclaimer variant: 'Sie ist keine'", "Sie ist keine ärztliche Beratung" in SKILL)
check("sport.md: target = upper half of TDEE minus H1", "(upper half of the TDEE range) − (H1 range)" in SPORT)
check("sport.md: sessions > 60 min count toward +0.3", "Sessions longer than 60 min count toward" in SPORT)
check("supplements.md: ISSN note covers protein powder", "protein powder [Q1]" in SUPPS)
check("Referral: German refusal says 'keinen Ernährungsplan'", "keinen Ernährungsplan, auch keinen sanften" in SKILL)
check("Block 1: no plan promise before Block 2", "Do not promise a plan before Block 2" in SKILL)
check("ANALYSIS: A/B question fixed in German", "Soll ich (A) diesen Plan anpassen oder (B)" in SKILL)
check("claims.md: disease reference is step 0", "0. **Disease reference first.**" in CLAIMS)
check("User study numbers restated 'laut deinem Text'", "laut deinem Text" in SKILL and "laut deinem Text" in SUPPS and "laut deinem Text" in CLAIMS)
check("Seller conflict of interest is mandatory", "**Mandatory sentence**" in SUPPS)
check("No verdict as opening sentence", "Do not open with a recommendation or a rejection" in SUPPS)

# --- report ---------------------------------------------------------------------
failed = [r for r in results if not r[1]]
for name, ok, detail in results:
    if not ok:
        print(f"FAIL  {name}" + (f"  — {detail}" if detail else ""))
print(f"\n{len(results) - len(failed)}/{len(results)} checks passed")
sys.exit(1 if failed else 0)
