#!/usr/bin/env python3
"""Build the self-contained project reference from the goal files.

Run from the skill folder:  python3 project-setup/build-reference.py

The project route uploads exactly one knowledge file, so every cross-reference
the goal files make to a sibling file has to be rewritten to point at a section
of this one. REWRITES below is that map; check-consistency.py asserts that the
built file contains no filename references at all.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
SKILL = HERE.parent

REWRITES = [
    # → the project instructions, which replace SKILL.md on this route
    ("the single-line note rule in SKILL.md",
     "the single-line note rule in the project instructions"),
    ("check it against the minimum preparation table in SKILL.md and name the compression to the user before continuing.",
     "check it against the Planning defaults table above and name the compression to the user before continuing."),
    ('apply the "Goal pace >30 % faster" and "ambitious goal" validation rules in SKILL.md',
     'treat it as a conflict under the rules in the project instructions'),
    ("this matches the count logic in SKILL.md UPDATE MODE",
     "this matches the count logic in the project instructions' update mode"),
    ("and is part of the SAFETY TRIAGE list in SKILL.md.",
     "and is part of the safety triage in the project instructions."),
    ("and are part of the SAFETY TRIAGE list in SKILL.md.",
     "and are part of the safety triage in the project instructions."),
    ("see the SAFETY TRIAGE fever row in SKILL.md, which governs",
     "see the fever row of the safety triage in the project instructions, which governs"),
    ("the SAFETY TRIAGE fever row in SKILL.md governs",
     "the fever row of the safety triage in the project instructions governs"),
    ("This is the one case where SKILL.md Rule 4 expects more than one goal file; for a single-modality goal, only that goal's file is loaded.",
     "This is the one case where more than one section applies; for a single-modality goal, read only that goal's section."),
    ("run the WEARABLE DATA CHECK in SKILL.md.",
     "run the wearable data check near the top of this file."),
    ("say so instead of comparing across it.\n\n\n",
     "say so instead of comparing across it.\n\n"),
    # → sections of this same file
    ("load `runner.md` and `strength.md` alongside it",
     "read the **Running** and **Strength** sections above alongside it"),
    ("load `runner.md` as primary, use `strength.md` for supplementary work",
     "treat **Running** as primary and use **Strength** for supplementary work"),
    ("load `strength.md` as primary, use `runner.md` principles for cardio programming",
     "treat **Strength** as primary and use **Running** for cardio programming"),
    # → the pace fallback, which now lives in the project instructions
    ("These values are the single source together with `assessment.json` → `pace_estimation_when_unknown`; both must always say the same thing.",
     "These values are the single source for the fallback bands; the project instructions point here for them."),
]

# The goal files defer to a table that lives in SKILL.md. The project route has
# no SKILL.md, so the table travels with the reference instead.
PLANNING_DEFAULTS = """## Planning defaults — runway and long-run demand

Declared planning defaults, not measured thresholds: they describe how much
runway a plan of this kind usually needs. A shortfall is a conflict to explain
and solve with the user, never a verdict on what they are capable of. An athlete
who already has the base and the long-session capability for the distance can be
given a shortened build or a taper instead — name the compromise.

| Distance | Usual weeks to the event | Assumed starting base | Longest session the plan must fit |
|---|---|---|---|
| 5k | 6 | Runs 2–3×/week | 45–60 min |
| 10k | 8 | Runs 3×/week, ~20 km/week | 60–75 min |
| Half marathon | 12 | Runs 3×/week, ~25 km/week, has completed 10 km | 90–120 min |
| Marathon | 16 (20 if the base is thin) | Runs 4×/week, ~40 km/week, has completed a half | 150–180 min |
| Trail / Ultra | 20 | Intermediate+, marathon or long trail experience | time-based |

---

"""

# Ported from the Claude edition v2.6.0. In SKILL.md these sections sit in the
# rule set; the project route carries them here, next to the goal sections.
UPDATE_SECTIONS = """## Wearable data check — before any wearable number changes the plan

Applies in every mode, whenever a wearable value (HRV, recovery/readiness score, resting HR, sleep score, training status) is about to change a session, a week or a phase. It runs after the safety triage in the project instructions and before any update-mode adjustment. A wearable number is a measurement of the device as much as of the person — check the device before you believe the person changed.

**1. Ask, unless already answered** (one message, short):
- Same device and same firmware over the whole comparison window — including the period the "normal" value comes from? A watch or ring swap, a firmware update or a new app version all count.
- Worn the same way? Fit (looser strap at night slips), same wrist/finger, complete nights.
- Same kind of number? A nightly average and a morning spot reading are not comparable, and neither is one brand's HRV with another's. A chest-strap morning reading with the same protocol is the most dependable everyday setup; an overnight optical value from a watch or ring is more exposed to fit and device changes.
- Does anything else move with it? Resting HR against its usual value, sleep, how the legs feel, how the last sessions went at the same effort.

**2. Decide what the number may do:**

| Situation | What the number may do |
|---|---|
| Device, firmware, fit or measurement type changed inside the window — or the user does not know | Nothing. Say the old baseline no longer applies, keep the current plan, steer by resting HR, sleep, feel and session RPE, and rebuild the baseline on the new device over the next 3–4 weeks. |
| Data clean, but the number moves alone — resting HR, sleep, feel and performance all unremarkable | Nothing beyond a note. Keep the plan, keep watching. One metric alone never triggers a deload. |
| Data clean, and at least one independent signal agrees — resting HR clearly above usual, sleep worse, heavy legs, same effort feels harder | Swap the next hard session for an easy one. A deload week only if the picture persists for about a week. |

**3. Never invent a cause.** If you do not know why a value dropped, say so. "Probably accumulated load" is a guess; present it as one or leave it out.

Why this check, and why HRV still matters: HRV is the one readiness measure every athlete can afford, and measured consistently — chest strap, same time each morning, same position, same app — it is reliable enough to steer day-to-day intensity. The literature uses it exactly that way: a rolling 7-day average against the individual's normal range from a 3–4 week baseline, changing the next session's intensity rather than whole weeks. Compared with a predefined plan, HRV guidance performed at least as well in two 2021 meta-analyses, with fewer non-responders — the advantage is not a bigger average gain but fewer athletes who stall or dig a hole. It answers a different question than a lactate step test or spiroergometry: those set the zones, HRV says whether today is a day to use the top of them. What breaks it is inconsistent measurement — consumer watches and rings measured overnight disagree with each other and with ECG to different degrees, so a device swap looks exactly like a change in the athlete.

---

## Update rules — missed sessions, "too easy", wearable values

Apply in update mode, after the safety triage. Write no changed sessions while a question below is still open.

| Pattern | Action |
|---|---|
| 2+ sessions skipped — ask why first, unless the user already said; always ask how sleep and stress were in those weeks and whether that is over now, even when the reason is known | **Time or schedule, cause over, feels rested:** no volume cut. Resume at the last load actually completed — short sleep during the missed weeks is no reason to go below it. **Sleep still short or stress ongoing:** hold the last completed load and make the next hard session an easy one until sleep is back to normal. Either way, not at the progression the missed weeks would have reached, and never make up missed sessions. If it keeps happening, fit the plan to the days that really exist (fewer sessions). **Fatigue, illness, pain:** run the safety triage, then reduce volume ~20 %. |
| "Too easy" 2 weeks — only counts for weeks in which most planned sessions were actually done | Increase intensity/volume ~10 %. Sessions that feel easy after a break are freshness, not new fitness. Skipped sessions are an implementation problem, not a physiological non-response. |
| HRV, recovery or readiness trending down | Run the wearable data check above first. Act only as its table allows — never a deload week from the number alone. |

Every changed session is plan content: the disclaimer comes first. Describe logged sessions only as the log or the user describes them; add no details neither contains.

---

"""

HEADER = """# TheFitFuturist Training Reference

Reference material for the training coach project. Load only the section that
matches the goal: **Running**, **Strength**, or — for a mixed goal — all three,
because the Mixed section sits on top of the other two.

This file is self-contained. Everything the sections refer to is either in here
or in the project instructions; no other file is needed.

Version {version} · © 2026 TheFitFuturist — Sportive Growth Ltd. · CC BY-NC 4.0

---

## Disclaimer — output this before any plan content, in the user's language

> **Important:** This training plan is generated by an AI assistant and is for
> informational purposes only. It is not a substitute for professional medical or
> coaching advice. If you have any health conditions, injuries, or concerns,
> consult a qualified professional before starting. You follow this plan at your
> own risk.

German:

> **Wichtig:** Dieser Trainingsplan wurde von einer KI erstellt und dient
> ausschließlich zur Information. Er ersetzt keine ärztliche Beratung und keine
> Betreuung durch einen qualifizierten Trainer. Wenn du gesundheitliche
> Beschwerden, Verletzungen oder Bedenken hast, kläre das vor dem Start mit einer
> Fachperson ab. Du trainierst nach diesem Plan auf eigenes Risiko.

For any other language, translate the English version faithfully — every clause
must survive. Never shorten or soften it.

---

"""

SECTIONS = [
    ("Running", "goals/runner.md"),
    ("Strength", "goals/strength.md"),
    ("Mixed — the interference layer, read with Running and Strength", "goals/mixed.md"),
]


def main() -> int:
    version = re.search(r"version (\d+\.\d+\.\d+-chatgpt\.\d+)",
                        (SKILL / "SKILL.md").read_text(encoding="utf-8")).group(1)

    parts = [HEADER.format(version=version), PLANNING_DEFAULTS, UPDATE_SECTIONS]
    for title, rel in SECTIONS:
        body = (SKILL / rel).read_text(encoding="utf-8")
        if body.startswith("---"):
            body = body.split("---", 2)[-1].lstrip()
        parts.append(f"# {title}\n\n{body.rstrip()}\n\n---\n\n")

    text = "".join(parts)

    missed = []
    for old, new in REWRITES:
        if old not in text:
            missed.append(old[:60])
        text = text.replace(old, new)
    if missed:
        print("Rewrite target not found — the goal files changed:", file=sys.stderr)
        for m in missed:
            print("  ", m, file=sys.stderr)
        return 1

    leftovers = re.findall(r"`?\b(?:SKILL\.md|assessment\.json|runner\.md|strength\.md|mixed\.md)`?", text)
    if leftovers:
        print(f"Dangling file references remain: {sorted(set(leftovers))}", file=sys.stderr)
        return 1

    out = HERE / "tff-training-reference.md"
    out.write_text(text.rstrip() + "\n", encoding="utf-8")
    print(f"{out.name}: {len(text)} characters, no dangling references, version {version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
