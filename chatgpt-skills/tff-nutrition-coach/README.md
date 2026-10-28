# TFF Nutrition Coach — ChatGPT edition

Evidence-based nutrition plans for **healthy adults who train**: fat loss while keeping muscle, muscle gain, and endurance fuelling. The assistant runs a safety triage and a short assessment first, then builds energy, protein and carbohydrate targets as sourced ranges with example days, and adapts the plan from weekly feedback.

Version: **0.1.4-chatgpt.1**. It is built from the [TFF Nutrition Plan Skill v0.1.4](../../claude-skills/tff-ernaehrungsplan-skill/) for Claude and uses the same rules, sources and numbers.

> **Status: in validation, not released.**

## Why a separate edition

In a ChatGPT project, the files are not read in full. ChatGPT searches them and uses the passages it finds. In a test on 2026-10-28 with the Claude files, this went wrong:
- In one of two chats, ChatGPT wrote a full plan before asking about age, health or eating behaviour.
- It searched the web for studies and supermarket prices.
- It forecast the user's weight after four weeks.

This edition therefore puts the safety rules directly into the project instructions, which ChatGPT always reads. The detailed rule set moves into one reference file.

## Setup (about 3 minutes, every plan including Free)

1. Create a project in ChatGPT.
2. Open `PROJECT-INSTRUCTIONS.md`, copy all of it and paste it into the project's instructions field. It is 6,595 characters, under the 8,000 limit.
3. Upload `tff-nutrition-reference.md` as the only project file. Do not upload the Claude files as well.
4. Start every plan in a new chat inside that project.

The route uses one file, so it fits the Free plan's limit of five files per project. That leaves room for the three tracking files you save later.

**Gemini and other assistants:** the same two pieces work in a Gemini Gem or any assistant that takes instructions plus a knowledge file. This is not tested yet.

**ChatGPT Business/Enterprise with a Skills tab:** you can upload the Claude edition's ZIP as a skill. This is not tested yet; the project route above is the recommended one.

## Keeping the plan alive

After a plan, the assistant outputs three tracking files:

| File | What it holds |
|---|---|
| `nutrition-log.md` | morning weight, hunger 1–5, energy 1–5, whether you followed the plan |
| `health-flags.md` | warning signs over time, same format as the TFF training coach |
| `current-plan.md` | the short form: goal, energy target, protein, carbohydrate by day type |

Save all three into the project. In later chats the assistant reads them and switches to update mode.

## What is in the folder

| File | Content |
|---|---|
| `PROJECT-INSTRUCTIONS.md` | Instructions field text: safety triage, assessment, hard floors, output order, German disclaimer |
| `tff-nutrition-reference.md` | Built file: the full Claude skill (rules, goals, modifiers, sources, claims, supplements, formulas) in one file |
| `build-reference.py` | Rebuilds the reference file from the Claude edition |
| `check-consistency.py` | Release check |

## Changing the skill

Change the rules only in the Claude edition. Then run:

```bash
python3 chatgpt-skills/tff-nutrition-coach/build-reference.py
python3 chatgpt-skills/tff-nutrition-coach/check-consistency.py
```

The check fails in these cases:
- the reference file is out of date
- the instructions exceed 8,000 characters
- a safety wording in the instructions no longer matches the Claude SKILL.md word for word

## License

CC BY-NC 4.0. Free to use and adapt for personal use. Not for commercial use without permission.

*© 2026 TheFitFuturist — Sportive Growth Ltd. | [thefitfuturist.com](https://www.thefitfuturist.com)*
