# TFF Training Plan Skill (Basic) — v2.3.3

A ready-to-use Claude skill for personalized, evidence-based training plans. Upload the ZIP to Claude — Claude will run a structured assessment and generate a plan tailored to your goal, fitness level, schedule, and health history.

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

## Download

→ [tff-training-skill-v2.3.3.zip](./tff-training-skill-v2.3.3.zip)

## Setup

### Prerequisites
- Any Claude account (free or paid)
- "Code execution and file creation" enabled in Settings → Capabilities

### Installation (2 minutes)

**Option A — Direct download (recommended):**
1. Download [tff-training-skill-v2.3.3.zip](./tff-training-skill-v2.3.3.zip)
2. In Claude, go to **Settings → Customize → Skills**
3. Upload the ZIP file
4. Start a new chat and describe your training goal — Claude recognizes the skill automatically

**Option B — Clone the repo:**
```bash
git clone https://github.com/ChrisSportiveGrwoth/TheFitFuturist.git
```
Then ZIP the `claude-skills/tff-trainingsplan-skill/` folder and upload via Settings → Customize → Skills.

> Note: The ZIP must contain the skill folder at the root, not just the contents.

## Tracking your training

After your plan is generated, Claude outputs three files you can save for future sessions:

| File | Purpose |
|------|---------|
| `training-log.md` | Session-by-session log |
| `health-flags.md` | Pain/injury tracking with recurrence counts |
| `current-plan.md` | Active plan summary (phase, pace, HR zones, next session) |

In subsequent chats, Claude reads these files and enters Update Mode automatically — adjusting load based on what you report.

## License

© 2026 TheFitFuturist — Sportive Growth Ltd.
Licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — free for personal use, not for commercial use without permission.

Built by [TheFitFuturist](https://www.thefitfuturist.com) — AI-powered training, critically tested.

Follow on [Substack](https://thefitfuturist.substack.com) for updates and new skills.
