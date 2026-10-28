#!/usr/bin/env python3
"""Build the single project reference file from the Claude edition.

Run from the repo root:  python3 chatgpt-skills/tff-nutrition-coach/build-reference.py

The project route uploads one knowledge file, so the whole Claude skill is
concatenated into it: SKILL.md as section SKILL, every other file under a
heading with its path. Nothing is rewritten by hand, so the two editions cannot
drift; check-consistency.py fails when the built file is out of date.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
SOURCE = HERE.parent.parent / "claude-skills" / "tff-ernaehrungsplan-skill"
OUT = HERE / "tff-nutrition-reference.md"

FILES = [
    "goals/fat-loss.md",
    "goals/muscle-gain.md",
    "goals/endurance.md",
    "modifiers/age.md",
    "modifiers/sport.md",
    "reference/claims.md",
    "reference/sources.md",
    "reference/supplements.md",
]

HEADER = """# TheFitFuturist Nutrition Reference

Reference file for the TFF Nutrition Coach project in ChatGPT. Built from the
TFF Nutrition Plan Skill v{version}; do not edit by hand.

How to read it:
- Section **SKILL** is the full rule set. The project instructions summarise its
  safety rules; for everything else, this section decides.
- Every other section is headed `FILE: <path>`. When the rules name a file such
  as `goals/fat-loss.md`, read the section with that heading.
- "Knowledge" or "Project Knowledge" means the files saved in this project.
- Use only the numbers in this file. No web search for values, studies or prices.

"""


def strip_frontmatter(text):
    return re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S).strip()


def build():
    skill = (SOURCE / "SKILL.md").read_text()
    version = re.search(r"^version: (\S+)$", skill, re.M).group(1)
    parts = [HEADER.format(version=version), "# SECTION: SKILL\n", strip_frontmatter(skill)]
    for rel in FILES:
        parts.append(f"\n\n---\n\n# FILE: {rel}\n")
        parts.append(strip_frontmatter((SOURCE / rel).read_text()))
    data = json.loads((SOURCE / "assessment.json").read_text())
    parts.append("\n\n---\n\n# FILE: assessment.json\n\n```json\n")
    parts.append(json.dumps(data, ensure_ascii=False, indent=1))
    parts.append("\n```\n")
    return "".join(parts)


if __name__ == "__main__":
    text = build()
    if "--check" in sys.argv:
        sys.exit(0 if OUT.exists() and OUT.read_text() == text else 1)
    OUT.write_text(text)
    print(f"wrote {OUT.name}: {len(text):,} characters")
