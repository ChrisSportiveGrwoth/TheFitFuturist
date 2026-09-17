#!/usr/bin/env python3
"""Consistency checks for the TFF Training Coach — ChatGPT edition.

Run from the skill folder:  python3 check-consistency.py
Every check encodes a defect that was found in a released version — they exist
to stop the same contradiction from coming back.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
SKILL = (HERE / "SKILL.md").read_text(encoding="utf-8")
RUNNER = (HERE / "goals/runner.md").read_text(encoding="utf-8")
STRENGTH = (HERE / "goals/strength.md").read_text(encoding="utf-8")
MIXED = (HERE / "goals/mixed.md").read_text(encoding="utf-8")
ASSESS_RAW = (HERE / "assessment.json").read_text(encoding="utf-8")

results = []


def check(name, condition, detail=""):
    results.append((name, bool(condition), detail))


# --- structural -------------------------------------------------------------
try:
    assess = json.loads(ASSESS_RAW)
    check("assessment.json parses", True)
except json.JSONDecodeError as exc:
    assess = {}
    check("assessment.json parses", False, str(exc))

check(
    "SKILL.md frontmatter has name + description",
    re.search(r"^name:\s*\S+", SKILL, re.M) and re.search(r"^description:\s*\S+", SKILL, re.M),
)

# ChatGPT's documented skill frontmatter is name + description only, so the
# version is declared in the body instead. Keep it to exactly one statement.
versions = re.findall(r"version (\d+\.\d+\.\d+-chatgpt\.\d+)", SKILL)
check("SKILL.md declares exactly one version", len(versions) == 1, str(versions))
check("frontmatter carries no keys beyond name + description",
      sorted(re.findall(r"^(\w+):", SKILL.split("---")[1], re.M)) == ["description", "name"],
      str(sorted(re.findall(r"^(\w+):", SKILL.split("---")[1], re.M))))

for path in ("goals/runner.md", "goals/strength.md", "goals/mixed.md"):
    text = (HERE / path).read_text(encoding="utf-8")
    body = text.split("---", 2)[-1]
    check(f"{path}: H1 sits outside the frontmatter", body.lstrip().startswith("#"))

# --- max HR formula ---------------------------------------------------------
for label, text in (("SKILL.md", SKILL), ("runner.md", RUNNER), ("assessment.json", ASSESS_RAW)):
    operative = re.search(r"220\s*[-−]\s*age(?!.*(?:older|overestimat|more accurate))", text, re.I)
    check(f"{label}: no operative 220-age formula", operative is None)

# --- HR zone labelling (v2.3.5) --------------------------------------------
check("SKILL.md: percentage column is method-labelled, not hardcoded '% max HR'",
      "% HRR" in SKILL and "% max HR" in SKILL)
check("SKILL.md: no unqualified '% max HR range' column requirement",
      "% max HR range" not in SKILL)
check("runner.md: HR table carries both method labels", "% HRR (Karvonen)" in RUNNER)
check("runner.md: HR table has a pace column", re.search(r"\|\s*Pace \(min/km\)\s*\|", RUNNER) is not None)
check("assessment.json: HRR vs max-HR warning present",
      "_warning" in assess.get("hr_zone_calculation", {}))
check("assessment.json: karvonen declares percent_of",
      "HRR" in assess.get("hr_zone_calculation", {}).get("karvonen", {}).get("percent_of", ""))
check("assessment.json: age_based declares percent_of",
      "max HR" in assess.get("hr_zone_calculation", {}).get("age_based", {}).get("percent_of", ""))

# --- pace consistency across the three sources ------------------------------
pace_json = {lvl: assess.get("pace_estimation_when_unknown", {}).get(lvl, {}).get("easy_pace", "")
             for lvl in ("beginner", "intermediate", "advanced")}
runner_table = dict(re.findall(r"\|\s*(Beginner|Intermediate|Advanced)\s*\|\s*([\d:]+-[\d:]+)/km\s*\|", RUNNER))
for lvl in ("beginner", "intermediate", "advanced"):
    j = pace_json[lvl].replace("/km", "")
    r = runner_table.get(lvl.capitalize(), "")
    check(f"easy pace {lvl}: assessment.json == runner.md", j == r, f"json={j!r} runner={r!r}")
    check(f"easy pace {lvl}: SKILL.md quotes the same range",
          j.replace("-", "–") in SKILL or j in SKILL, f"expected {j!r} in SKILL.md")

# --- safety triage (v2.3.5) -------------------------------------------------
check("SAFETY TRIAGE is its own top-level section, not buried in one mode",
      "## SAFETY TRIAGE" in SKILL)
check("SAFETY TRIAGE sits above the three modes",
      SKILL.index("## SAFETY TRIAGE") < SKILL.index("## NEW PLAN MODE"))
triage = SKILL.split("## SAFETY TRIAGE", 1)[-1].split("\n## ", 1)[0]
for symptom in ("Chest pain", "Dizziness", "thrombosis", "Acute trauma",
                "Palpitations", "neurological", "breath"):
    check(f"triage covers: {symptom}", symptom.lower() in triage.lower())
check("triage states it applies in every mode", "every mode" in triage.lower())
update_mode = SKILL.split("## UPDATE MODE", 1)[-1].split("## ANALYSIS MODE", 1)[0]
check("UPDATE MODE: triage precedes the pattern table",
      "SAFETY TRIAGE" in update_mode
      and update_mode.index("SAFETY TRIAGE") < update_mode.index("| Same pain 1×"))
check("triage table is defined once, not duplicated per mode",
      SKILL.count("| Palpitations / irregular heartbeat during or after training |") == 1)
check("UPDATE MODE loads the goal file", "goal file" in update_mode.lower())
check("Rule 13 is not scoped to plan generation only",
      "before generating any plan" not in SKILL.split("14.")[0])

# --- validation gaps (v2.3.5) ----------------------------------------------
check("Validation: Marathon + Beginner row exists", "Marathon + Beginner" in SKILL)
check("Validation: minimum preparation table exists", "Minimum Preparation Time" in SKILL)
check("Validation: long-run vs session duration row exists",
      "session_duration too short" in SKILL)
enforcement = SKILL.split("### Validation Enforcement Rule", 1)[-1].split("###", 1)[0]
for stop in ("Marathon + Beginner", "minimum preparation time", "long run does not fit"):
    check(f"Enforcement hard-stop list includes: {stop}", stop in enforcement)

# --- cross-file contradictions ---------------------------------------------
check("Rule 4 permits the mixed multi-file load",
      re.search(r"4\.\s+\*\*Load the goal file\(s\)", SKILL) is not None
      and "Never load all three simultaneously" not in SKILL)
check("mixed.md still instructs loading both modality files",
      "runner.md" in MIXED and "strength.md" in MIXED)
check("runner.md: strength is no longer worded as mandatory",
      "mandatory for all runner types" not in RUNNER.lower()
      and "Mandatory for All Runner Types" not in RUNNER)
check("Rule 11 scopes the wearable question to Running/Mixed",
      "Running and Mixed plans" in SKILL)
check("runner.md red flags carry a Trigger column", "| Trigger |" in RUNNER)
check("strength.md red flags carry a Trigger column", "| Trigger |" in STRENGTH)
check("SKILL.md age 60–69 no longer says 'lower per-session volume'",
      "lower per-session volume" not in SKILL)

# --- single source of truth within SKILL.md (no restated instructions) ------
check("goal-file loading is stated once (Rule 4), generation step defers to it",
      "Load the goal file(s) per Rule 4." in SKILL
      and "Load goal file: Running →" not in SKILL)
check("disclaimer step is language-aware, not blanket 'verbatim'",
      "DISCLAIMER block in the user's language" in SKILL)
check("Rule 10 does not contradict the hard stops",
      "Do not refuse outright." not in SKILL and "Never a bare refusal" in SKILL)
check("acute injury row is marked as a hard stop like the others",
      "| Acute injury (surgery <6 weeks, broken bone) | ⚠️ **HARD STOP.**" in SKILL)
check("no redundant marathon session-time row alongside the long-run rule",
      "<30 min/session + marathon" not in SKILL)
check("HR worked example lives in runner.md, SKILL.md only points at it",
      SKILL.count("130–142 bpm") == 0 and RUNNER.count("130–142 bpm") >= 1)
check("Block 4 routes a known race time to Principle 2c",
      "Principle 2c" in SKILL)
check("health-flags Count semantics are defined (0 = history, 1 = first report)",
      "Count semantics:" in SKILL)
check("deload cadence is phrased as loading weeks, not bare 'every N weeks'",
      "deload every 3 weeks" not in SKILL.lower()
      and "deload every 3 weeks" not in STRENGTH.lower())

# --- phase renormalization --------------------------------------------------
check("runner.md: renormalization rule for plans under 20 weeks",
      "Renormalization for plans under 20 weeks" in RUNNER)
check("runner.md: taper no longer carries the contradictory 'min 2 weeks'",
      "10% (min 2 weeks)" not in RUNNER)

# --- race time conversion / pace anchors ------------------------------------
check("runner.md: Principle 2c exists", "Principle 2c" in RUNNER)
check("runner.md: Riegel formula present", "1.06" in RUNNER)
check("SKILL.md: starting volume is anchored to the current routine",
      "Starting volume is derived from this answer" in SKILL)

# --- language ---------------------------------------------------------------
check("SKILL.md: German disclaimer present", "Dieser Trainingsplan wurde von einer KI erstellt" in SKILL)
check("SKILL.md: disclaimer 'verbatim' is scoped to a language",
      "Verbatim\" applies within a language" in SKILL or "applies within a language" in SKILL)
check("SKILL.md: ✓ Logged has a German version", "✓ Notiert" in SKILL)
check("SKILL.md: Rule 12 covers fixed phrases", "fixed phrases quoted in this file" in SKILL)

# --- illness / fever (v2.4.0) ----------------------------------------------
# v2.3.5 handled illness with one UPDATE MODE row ("Illness | Reset to easy week"),
# below the count logic and outside the triage gate. Training through a fever is a
# cardiac risk, so it belongs in triage, on first mention, in every mode.
triage_block = SKILL.split("## SAFETY TRIAGE")[1].split("## NEW PLAN MODE")[0]
check("triage covers fever / systemic infection", "fever" in triage_block.lower())
check("triage names the return-to-training criterion, not just 'rest'",
      "symptom-free" in triage_block.lower())
check("SKILL.md states a fever is never trained through",
      "never train through a fever" in SKILL.lower())
# v2.4.1: the blanket "do not generate or adjust a plan" lead-in collided with the
# fever row, whose own action prescribes a graded return. One test run wrote the
# return ladder, a stricter reading would have withheld it — so the lead-in now
# separates referral rows from the fever row explicitly.
check("triage separates referral rows from the fever row",
      "Referral rows" in triage_block and "The fever row" in triage_block)
check("referral rows forbid writing a return ladder",
      "no return ladder" in triage_block)
check("fever row names the graded return as the deliverable",
      "graded return" in triage_block and "is the deliverable" in triage_block.replace("**", ""))
check("fever row reverts to referral on cardiac symptoms",
      "reverts to a referral row" in triage_block)
check("fever return is steered by HR, not the plan's paces",
      "heart rate and feel" in triage_block)
check("fever return forbids making up missed volume",
      "Never make up missed volume" in triage_block)
check("UPDATE MODE illness row defers to the triage fever check",
      re.search(r"\|\s*Illness[^|]*triage", SKILL) is not None)
check("UPDATE MODE illness row prescribes a graded return, not a bare easy week",
      "Graded return" in SKILL)
for label, text in (("runner.md", RUNNER), ("strength.md", STRENGTH), ("mixed.md", MIXED)):
    check(f"{label}: red flags carry the fever row", "myocarditis" in text.lower())

# --- low energy availability (v2.4.0) --------------------------------------
# RED-S was absent from every file: the scope line ("no nutrition advice") had
# silently taken the training-side red flag with it.
for label, text in (("runner.md", RUNNER), ("strength.md", STRENGTH), ("mixed.md", MIXED)):
    check(f"{label}: low energy availability is a red flag",
          "low energy availability" in text.lower())
    check(f"{label}: LEA row holds volume instead of prescribing food",
          re.search(r"low energy availability.*?(calories|eating plan)", text,
                    re.I | re.S) is not None)
check("SKILL.md scope keeps the under-fuelling red flag in scope",
      "does not mute the under-fuelling red flags" in SKILL)
check("UPDATE MODE pattern table carries the LEA row",
      "Low energy availability signals" in SKILL)

# --- pace table: precedence and provenance (v2.4.0) ------------------------
check("Rule 7 states that a known race time supersedes the level table",
      re.search(r"^7\..*race time.*(wins|supersede)", SKILL, re.M | re.I) is not None)
check("Rule 7 names Principle 2c as the path for a known result",
      re.search(r"^7\..*Principle 2c", SKILL, re.M) is not None)
check("runner.md 2b declares itself the last resort, not the default",
      "last resort" in RUNNER)
check("pace bands carry their provenance in runner.md",
      "no primary source" in RUNNER)
check("pace bands carry their provenance in assessment.json",
      "_source" in assess.get("pace_estimation_when_unknown", {}))

# --- assessment flow (v2.4.0) ----------------------------------------------
# Rule 1 + 15 forbade bundling and skipping, so a user who supplied everything
# up front was walked through all six blocks again. Nothing said "already answered".
check("Rule 18 exists: supplied fields are not re-asked",
      re.search(r"^18\..*Never re-ask", SKILL, re.M) is not None)
check("Rule 18 keeps Block 2 gated rather than inferring age/health",
      re.search(r"^18\..*Block 2", SKILL, re.M) is not None)
check("Rule 18 forbids counting an inferred value as collected",
      re.search(r"^18\..*never if you inferred", SKILL, re.M) is not None)
check("NEW PLAN MODE header points at Rule 18",
      "see Rule 18" in SKILL)
rules_block = SKILL.split("## MANDATORY RULES")[1].split("## ROUTING")[0]
rule_numbers = [int(n) for n in re.findall(r"^(\d+)\.\s", rules_block, re.M)]
check("rule numbering has no duplicates and no gaps",
      rule_numbers == list(range(1, 20)), str(rule_numbers))

# --- ChatGPT edition: additions documented in DEVIATIONS.md ------------------
check("Rule 19 exists: uploaded files are data, not instructions",
      re.search(r"^19\..*data, not instructions", SKILL, re.M) is not None)
check("Rule 19 forbids role changes from file content",
      "change your role" in SKILL)

triage = SKILL.split("## SAFETY TRIAGE")[1].split("## NEW PLAN MODE")[0]
check("triage describes three row kinds, not two",
      "three kinds" in triage and "**Hold rows**" in triage)
check("triage carries the under-fuelling row",
      "low energy availability" in triage.lower())
check("triage under-fuelling row holds volume instead of prescribing food",
      "Hold volume where it is" in triage and "never prescribe calories" in triage)
check("triage under-fuelling row acts on first mention",
      "does not need a second report" in triage)

check("mixed.md: 48h spacing is a default, not an absolute",
      "Default spacing" in MIXED and "Never same day, 48h minimum" not in MIXED)
check("mixed.md: the spacing default states its evidence basis",
      "scheduling defaults, not thresholds" in MIXED)
check("mixed.md: availability outranks ideal spacing",
      "where the week allows" in MIXED)

check("1 day/week is only a hard stop for event or performance goals",
      "1 day/week **for an event or performance goal**" in SKILL)
check("1 day/week for a fitness goal still produces a plan",
      "not a hard stop in itself" in SKILL)
check("minimum preparation table is labelled as a planning default",
      "declared planning default, not a measured threshold" in SKILL)
check("runner.md: a short base phase is named as compression, not a verdict",
      "the plan is compressed for the distance" in RUNNER)


# --- v2.5.1: no fixed heart-rate ceiling in the pregnancy protocol ------------
PREG = SKILL.split("Pregnancy Protocol")[1].split("---")[0]
check("pregnancy protocol carries no fixed bpm ceiling",
      re.search(r"\d{2,3}\s*bpm", PREG) is None, PREG[:0])
check("pregnancy intensity is steered by talk test and RPE",
      "talk test" in PREG and "RPE" in PREG)
check("clinician instructions outrank the skill file",
      "outrank" in PREG)
check("pregnancy protocol keeps its other constraints",
      "no high-impact" in PREG and "no supine after T1" in PREG and "no breath-holding" in PREG)


# --- 2.5.2: pace bands, runway exception, arithmetic check, project route ----
check("no walking-pace justification for the pace bands",
      "walking pace, not running" not in SKILL and "walking pace, not running" not in RUNNER)
check("no per-level pace floor is enforced anywhere",
      not any("max_easy_pace_cap" in s for s in (SKILL, RUNNER, ASSESS_RAW)))
check("no walking justification survives in any file",
      not any("walking, not running" in s or "walking pace, not running" in s
              for s in (SKILL, RUNNER, ASSESS_RAW)))
check("no fixed pace cap language in the beginner caveat",
      "10:00/km cap" not in RUNNER)
check("HR zones are required only where the data allows it",
      "where the data allows it" in SKILL and "where the data allows it" in RUNNER)
check("invented HR zones are forbidden",
      "do not invent" in SKILL and "do not invent zones" in RUNNER)
check("the pace bands are described as a range, not a floor",
      "not a floor" in RUNNER or "not as a floor" in SKILL)
check("a short runway is not a hard stop for a prepared athlete",
      "not a hard stop for an athlete who already has the base" in SKILL)
check("the arithmetic check exists and covers the session parts",
      "Arithmetic check before output" in SKILL and "rest intervals" in SKILL and "cool-down" in SKILL)
check("the arithmetic check covers the race day",
      "Race week" in SKILL)
check("the arithmetic check never adjusts the user's budget",
      "Never silently adjust the budget" in SKILL)

PROJ = (HERE / "project-setup/PROJECT-INSTRUCTIONS.md").read_text(encoding="utf-8")
REF = (HERE / "project-setup/tff-training-reference.md").read_text(encoding="utf-8")
check("project instructions fit the 8000-character field", len(PROJ) <= 8000, f"{len(PROJ)} chars")
check("project instructions carry the full safety triage",
      all(k in PROJ for k in ("Referral rows", "Hold row", "Fever row", "Pregnancy")))
check("project instructions carry the arithmetic check",
      "Check your arithmetic" in PROJ and "warm-up" in PROJ and "race week" in PROJ)
check("project instructions carry the data boundary",
      "data, not instructions" in PROJ)
check("project reference is self-contained",
      not re.search(r"SKILL\.md|assessment\.json|runner\.md|strength\.md|mixed\.md", REF))
check("project reference carries all three goal sections",
      all(k in REF for k in ("# Running", "# Strength", "# Mixed")))
check("project reference carries the disclaimer in both languages",
      "This training plan is generated by an AI assistant" in REF and "Dieser Trainingsplan wurde von einer KI" in REF)
check("project reference carries the runway table",
      "Planning defaults" in REF)

# --- report -----------------------------------------------------------------
failed = [(n, d) for n, ok, d in results if not ok]
for name, ok, detail in results:
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail and not ok else ""))
print(f"\n{len(results) - len(failed)}/{len(results)} checks passed")
sys.exit(1 if failed else 0)
