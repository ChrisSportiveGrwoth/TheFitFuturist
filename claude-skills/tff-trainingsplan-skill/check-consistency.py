#!/usr/bin/env python3
"""Consistency checks for the TFF Training Plan Skill.

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

versions = re.findall(r"^version:\s*(\S+)", SKILL, re.M)
check("SKILL.md declares exactly one version", len(versions) == 1, str(versions))

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

# --- report -----------------------------------------------------------------
failed = [(n, d) for n, ok, d in results if not ok]
for name, ok, detail in results:
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail and not ok else ""))
print(f"\n{len(results) - len(failed)}/{len(results)} checks passed")
sys.exit(1 if failed else 0)
