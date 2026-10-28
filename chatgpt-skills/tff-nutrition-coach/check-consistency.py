#!/usr/bin/env python3
"""Release check for the ChatGPT edition of the nutrition skill.

Run from the repo root:  python3 chatgpt-skills/tff-nutrition-coach/check-consistency.py

The rule set lives in the Claude edition. This check makes sure the project
instructions fit the ChatGPT field, quote the safety wordings verbatim from the
Claude SKILL.md, and that the reference file is rebuilt from the current source.
"""
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).parent
SOURCE = HERE.parent.parent / "claude-skills" / "tff-ernaehrungsplan-skill"
INSTR = (HERE / "PROJECT-INSTRUCTIONS.md").read_text()
SKILL = (SOURCE / "SKILL.md").read_text()
README = (HERE / "README.md").read_text()

results = []


def check(name, ok):
    results.append((name, bool(ok)))


# 1. Fits the ChatGPT instructions field
check("instructions <= 8000 characters", len(INSTR) <= 8000)

# 2. Reference file is current
built = subprocess.run([sys.executable, str(HERE / "build-reference.py"), "--check"])
check("tff-nutrition-reference.md rebuilt from current source", built.returncode == 0)

# 3. Safety wordings quoted verbatim from the Claude SKILL.md
skill_de_disclaimer = [l for l in SKILL.splitlines() if l.startswith("> **Wichtig:**")]
check("German disclaimer present in SKILL.md", len(skill_de_disclaimer) == 1)
check("German disclaimer verbatim in instructions",
      skill_de_disclaimer and skill_de_disclaimer[0] in INSTR)

VERBATIM = [
    "Wie alt bist du, und welches Geschlecht soll ich für die Energieformel verwenden?",
    "Hast du Erkrankungen, nimmst du Medikamente, oder bist du schwanger oder stillst du?",
    "Hattest du schon einmal ein schwieriges Verhältnis zum Essen — zum Beispiel starkes Einschränken, Essanfälle, Erbrechen, Abführmittel oder Training, um Essen auszugleichen?",
    "Bitte sprich mit deinen Eltern und geht gemeinsam in eine Kinder- und Jugendarztpraxis oder eine sportmedizinische Praxis.",
    "Deshalb erstelle ich dir keinen Ernährungsplan, auch keinen sanften, und nenne keine Kalorien-, Makro- oder Gewichtszahlen.",
    "Kein Defizit mehr: Iss mehr als in der Abnehmphase, nach deinem Hunger, und lass rund ums Training keine Mahlzeit aus.",
    "Soll ich (A) diesen Plan anpassen oder (B) einen neuen von Grund auf erstellen?",
]
for phrase in VERBATIM:
    check(f"in SKILL.md and instructions: {phrase[:50]}…", phrase in SKILL and phrase in INSTR)

# 4. Every referral and hold signal of the triage is named in the instructions
TRIAGE = ["eating disorder", "vomiting", "laxatives", "BMI below 18.5", "pregnancy",
          "breastfeeding", "under 18", "insulin", "kidney", "GLP-1", "anticoagulants",
          "MAO inhibitors", "lithium", "coeliac", "allergy", "periods", "bone stress",
          "infections", "constant hunger"]
for word in TRIAGE:
    check(f"triage signal named: {word}", word in INSTR)

# 5. Hard floors match the Claude edition
check("floor 1,200 kcal in both", "1,200 kcal" in INSTR and "1,200 kcal" in SKILL)
check("floor is the higher value, never the sum",
      "never their sum" in INSTR and "never their sum" in SKILL)
check("rate cap 1 % per week", "at most 1 % of body weight per week" in INSTR)
check("no fasts over 24 h", "fasts over 24 h" in INSTR)
check("no deficit 2 weeks before a key race", "2 weeks before a key race" in INSTR)

# 6. ChatGPT-specific guard rails (findings from the app test, 2026-10-28)
check("no web search", "No web search" in INSTR)
check("no shop or brand names", "No product, brand, shop or supermarket names" in INSTR)
check("no result forecasts", "No result forecasts" in INSTR)
check("no number before Blocks 1-4", "before Blocks 1–4 are answered" in INSTR)
check("first reply has no plan and no number", "first reply contains no plan and no number" in INSTR)

check("values derived from amounts, never fitted to the target",
      "Never adjust values to hit the target" in INSTR and "same values" in INSTR)
check("disclaimer in every reply with a calculated number",
      "Every reply that contains a number calculated for this user carries the disclaimer" in INSTR)

# 7. Output order and tracking files
for token in ["nutrition-log.md", "health-flags.md", "current-plan.md", "✓ Notiert"]:
    check(f"output names {token}", token in INSTR)

# 8. Versions agree
src_version = re.search(r"^version: (\S+)$", SKILL, re.M).group(1)
check("instructions version matches source", f"v{src_version}-chatgpt." in INSTR)
check("README version matches source", f"{src_version}-chatgpt." in README)

failed = [name for name, ok in results if not ok]
for name, ok in results:
    if not ok:
        print(f"FAIL  {name}")
print(f"\n{len(results) - len(failed)}/{len(results)} checks passed")
sys.exit(1 if failed else 0)
