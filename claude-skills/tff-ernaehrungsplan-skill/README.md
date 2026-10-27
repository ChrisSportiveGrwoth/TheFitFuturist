# TFF Nutrition Plan Skill (Basic) — v0.1.2

> **Status: in validation, not released.** There is no download yet. The ZIP is published only after the validation in the TheFitFuturist editorial repo passes.

A Claude skill for evidence-based nutrition plans for **healthy adults who train**. Claude runs a structured assessment with a safety triage first, then builds energy, protein and carbohydrate targets as sourced ranges with example days, and adapts the plan from weekly feedback.

## What it does

**Three goals:**
- **Fat loss while keeping muscle**: a rate of 0.5–1.0 % body weight per week, protein by training status, strength training as part of the rationale
- **Muscle gain / fitness**: a small surplus as a declared starting value, protein ranges from the ISSN position stands
- **Endurance performance and fuelling**: carbohydrate by training load, fuelling before/during/after sessions, fluid and sodium, race week

**Age and sport shift the numbers.** Protein per meal rises with age, and from 65 there is a protein minimum. Strength athletes sit in the upper half of a range. Endurance athletes get carbohydrate periodised by day type.

**Key features:**
- Every number carries a source code (Q = published source read in the original, H = declared heuristic that the weekly check corrects): `reference/sources.md`
- Safety triage on first mention, in every mode. It refers on for eating disorders, underweight, pregnancy, under-18s, insulin or other hypoglycaemic medication, kidney disease, GLP-1 and other nutrition-relevant medication, and diet-treated conditions. On signs of RED-S it holds the plan: no further deficit.
- Hard floors that cannot be negotiated: not below the estimated resting energy expenditure, not below 1,200 kcal, at most 1 % weight loss per week, no fasts over 24 h, no deficit in the two weeks before a key race
- Health-claim guard rails: effects are reported as study findings or in the approved EU wording. The skill uses no disease references, names no products, brands or shops, and promises no results (`reference/claims.md`)
- Supplements are tiered (A / B / need-based / C) and sourced. Food comes first. Vegan users always get a B12 notice, and the skill never suggests iron without a lab value (`reference/supplements.md`)
- Supplement studies are never given a blanket verdict: the skill names the population, dose, duration and outcome, asks about funding, and suggests reading the abstract
- Update mode works from 7-day weight averages, and adherence comes before calories
- Analysis mode checks plans from ChatGPT, apps or coaches
- Uploaded plans and files are treated as data, never as instructions

**Out of scope:** medical nutrition therapy, people under 18, pregnancy and breastfeeding, diagnosed conditions treated with diet, writing training plans. Training data from the [TFF Training Plan Skill](../tff-trainingsplan-skill/) (`current-plan.md`) is read as input.

## Files

| File | Content |
|---|---|
| `SKILL.md` | Rules, routing, safety triage, hard floors, assessment, plan generation, update and analysis mode, disclaimer |
| `goals/fat-loss.md` · `goals/muscle-gain.md` · `goals/endurance.md` | Principles and ranges per goal |
| `modifiers/age.md` · `modifiers/sport.md` | Age bands, sport categories, DGE activity factors |
| `reference/sources.md` | Source register Q1–Q25, heuristics H1–H4, funding notes |
| `reference/claims.md` | Approved EU health claims (EN + official German wording), pattern table, banned wording |
| `reference/supplements.md` | Tiers, reference values, procedure for user-supplied claims |
| `assessment.json` | Options, Mifflin-St Jeor formula, PAL table, all ranges with `_source`, worked examples |
| `check-consistency.py` | Release check: every number has a source, the ranges match across files, safety comes before the modes, the disclaimer is complete |

## Consistency check

```bash
python3 claude-skills/tff-ernaehrungsplan-skill/check-consistency.py
```

Must report all checks passed before any release.

## License

CC BY-NC 4.0. Free to use and adapt for personal use. Not for commercial use without permission.

*© 2026 TheFitFuturist — Sportive Growth Ltd. | [thefitfuturist.com](https://www.thefitfuturist.com)*
