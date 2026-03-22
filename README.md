# TFF Training Plan Skill (Basic) — v2.3.2

A ready-to-use Claude skill for personalized, evidence-based training plans. Paste into your Claude Project Instructions — Claude will run a structured assessment and generate a plan tailored to your goal, fitness level, schedule, and health history.

## What it does

Guides Claude through a 6-block conversational assessment before generating any plan. Covers goal and event, age and health, availability, fitness level, complementary training, and HR/wearable data. No plan is generated until the minimum required inputs are collected.

**Three goal types included:**
- **Running / Endurance** — 5k through ultra, with HR zones, pacing, periodization, and injury prevention
- **Strength / Muscle Building** — progressive overload, rep ranges, RPE guidance
- **Mixed / Concurrent** — interference management for runners who also lift, or vice versa

**Key features:**
- Personalized HR zones (Z1–Z5) with actual bpm values in every running plan
- Phase-based periodization (Base / Build / Peak / Taper for event plans)
- Evidence-based complementary strength work derived from injury history and goal
- Update mode: tell Claude how sessions went, it adjusts the plan
- Analysis mode: paste an existing plan, Claude critiques and improves it

## Setup

**Step 1 — Project Instructions**

Copy the full contents of `SKILL.md` into your Claude Project's *Instructions* field.

**Step 2 — Project Knowledge**

Upload all of the following to your Claude Project's *Knowledge* section:
- `assessment.json`
- `goals/runner.md`
- `goals/strength.md`
- `goals/mixed.md`

> You can upload all three goal files or just the one matching your goal. Claude only loads the relevant file per Rule 4.

**Step 3 — Start a conversation**

Open a new chat in the project. Claude will automatically detect mode (New Plan / Update / Analysis) and begin the assessment.

## Tracking your training

After your plan is generated, Claude outputs three files to save to Project Knowledge:

| File | Purpose |
|------|---------|
| `training-log.md` | Session-by-session log |
| `health-flags.md` | Pain/injury tracking with recurrence counts |
| `current-plan.md` | Active plan summary (phase, pace, HR zones, next session) |

In subsequent chats, Claude reads these files and enters Update Mode automatically — adjusting load based on what you report.

## File structure

```
tff-training-skill-v2.3.2/
├── SKILL.md              ← Paste into Project Instructions
├── assessment.json       ← Upload to Project Knowledge
├── README.md
├── CHANGELOG.md
└── goals/
    ├── runner.md         ← Upload to Project Knowledge
    ├── strength.md       ← Upload to Project Knowledge
    └── mixed.md          ← Upload to Project Knowledge
```

## License

© 2026 TheFitFuturist — Sportive Growth Ltd.
Licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — free for personal use, not for commercial use without permission.

Built by [TheFitFuturist](https://www.thefitfuturist.com) — AI-powered training, critically tested.

Follow on [Substack](https://thefitfuturist.substack.com) for updates and new skills.
