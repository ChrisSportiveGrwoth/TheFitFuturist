# TFF Training Coach — ChatGPT edition

A ready-to-upload ChatGPT skill for personalized, evidence-based training plans:
running, strength, and mixed (concurrent) goals. It runs a structured assessment
first, then writes the plan, then adapts it from what you report back.

Derived from the [TFF Training Plan Skill v2.5.1](../../claude-skills/tff-trainingsplan-skill/)
for Claude. Same sports-science core, same safety triage. The differences are
documented in [DEVIATIONS.md](./DEVIATIONS.md) — read that file before assuming
the two editions behave identically.

Version: **2.5.1-chatgpt.1**

## Before you start: can your account install this?

OpenAI currently documents skills for **Business, Enterprise, Healthcare and Edu**
accounts. Free, Go, Plus and Pro are not listed as supported plans. The rollout has
been uneven, so check your own account rather than assuming from the plan name:

> Sidebar → **Plugins** → **Skills** tab → **Create** → **Upload from your computer**

If that path does not exist for you, the skill cannot be installed on your account
yet — no workaround changes that, including asking ChatGPT to build one for you.
Use the project fallback below instead.

## Install (about 2 minutes)

1. Download `tff-training-coach.zip` from the
   [latest release](https://github.com/ChrisSportiveGrwoth/TheFitFuturist/releases/latest).
2. In ChatGPT: **Plugins → Skills → Create → Upload from your computer**.
3. Wait for the upload scan to finish.
4. Start a new chat and describe your training goal. ChatGPT picks the skill up
   from the request; you can also select it explicitly.

## Fallback: use it in a ChatGPT Project

Projects work on every plan, including Free. This route gives you the same
instructions without the skill mechanism:

1. Create a project.
2. Paste the core rules from `SKILL.md` into the project instructions.
   **Note the limit: project instructions hold 8,000 characters**, and `SKILL.md`
   is longer than that — you will have to shorten it. Keep the safety triage,
   the mandatory rules and the assessment blocks; those carry the behavior.
3. Upload the goal file you need (`goals/runner.md`, `goals/strength.md`, or for
   mixed goals all three) as project files. File limits per project: 5 on Free,
   25 on Plus and Go, 40 on Pro and above.
4. Run every training chat inside that project.

This is a weaker setup than the skill — the model reads the files rather than
having them routed — but it works today on any account.

## Keeping the plan alive

After a plan is generated, the skill outputs three tracking files:

| File | What it holds |
|---|---|
| `training-log.md` | your sessions as you report them |
| `health-flags.md` | pain, complaints and warning signs over time |
| `current-plan.md` | the short form: phase, paces, HR zones |

Save all three into a ChatGPT Project and run follow-up chats inside it. Then the
skill reads them, recognizes the running plan and goes into update mode instead of
starting over.

Without a project there is no memory between chats: you get a fresh plan, not an
adapted one. If you prefer to work without a project, paste the contents of
`current-plan.md` and `training-log.md` at the start of each new chat.

## What is in the package

```
tff-training-coach/
├── SKILL.md              assessment, safety triage, planning, update and analysis modes
├── assessment.json       question logic and few-shot examples
├── goals/
│   ├── runner.md         running: intensity distribution, periodization, pacing, HR zones
│   ├── strength.md       strength and hypertrophy: overload, volume, exercise selection
│   └── mixed.md          the interference layer on top of both
├── DEVIATIONS.md         every difference from the Claude edition, with reasons
└── README.md
```

## Requirements and limits

- Adults only. Not for diagnosis, rehabilitation programming, or nutrition plans.
- The skill asks before it plans. If you refuse the health questions, you get a
  general example, not a personal plan — that is deliberate.
- Health data you enter is processed by OpenAI under your account settings. Check
  your privacy settings before the first assessment, especially if you intend to
  upload wearable exports.

## Disclaimer

**Use at your own risk.** This is an instruction set for a language model, not a
coach and not a medical device. Output varies between runs, model versions and
contexts. Nothing here is medical, health or professional coaching advice. Consult
a qualified professional before starting any training program. TheFitFuturist and
Sportive Growth Ltd. accept no liability for injury, health issues or other damage
arising from use of this skill or the plans it generates.

## License

© 2026 TheFitFuturist — Sportive Growth Ltd.
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — free for personal
use and adaptation, not for commercial use without permission.
