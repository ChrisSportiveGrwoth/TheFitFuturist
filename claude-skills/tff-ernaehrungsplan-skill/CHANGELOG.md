# CHANGELOG — TFF Nutrition Plan Skill

Format: append only. Never delete entries.

## v0.1.1 — 2026-10-27 — Fixes from validation stage 1

Stage 1 (12 personas, simulated by Sonnet, graded by a separate model against criteria written beforehand): 11 of 12 green, with no ❌ on triage, floors or health claims. P6 was red because a personalised weight-loss rate appeared before the disclaimer. Fixes for the findings that came from the skill text:

- Rule 3: the disclaimer comes before every number calculated for this user, HARD STOP comparisons included. During the assessment the skill calculates nothing aloud.
- No time-to-goal estimates ("10 kg in 15–30 Wochen"). HCVO Art. 12 b prohibits them; the skill names the weekly rate and a checkpoint date instead.
- The energy floor is the higher of resting energy and 1,200 kcal, never their sum. A requested rate is always also shown as % body weight per week.
- New N rules in `sources.md` for food composition values, the 4/4/9 conversion, BMI and cost estimates. Previously Rule 5 contradicted the example days that Rule 17 requires.
- Rule 5: no source code on a statement the source does not make. Statements that are the skill's own choice are labelled as such.
- GLP-1 referral gives both reasons: medication and diet interact, and Q5 does not cover it.
- Block 2 always asks all three questions. A named target weight is checked silently against BMI 18.5.
- `sport.md`: no interpolated PAL addition for 1–3 sessions.
- `endurance.md`: energy per day type follows from the macros. H3 default: if the highest-load block is unknown, the final 5 weeks stay deficit-free.
- `claims.md`: the pattern table now uses the official German protein wording.
- `supplements.md`: Tier C refers to marketing categories, never to a single ingredient (ashwagandha stays "not rated").
- Disclaimer variant for answers without a plan; every clause stays.
- Total protein per day comes before the per-meal values, and the meal rhythm from Block 5 is respected.

## v0.1.0 — 2026-10-27 — First version, in validation

Not released. Built from the spec in the TheFitFuturist editorial repo. It was written in parallel to the article *KI-Ernährungsplan erstellen* (thefitfuturist.com/training-analyse/ki-ernaehrungsplan-erstellen/).

- Structure mirrors the TFF Training Plan Skill v2.5.5. It has 18 mandatory rules, a safety triage above all modes, a 6-block assessment with a non-skippable Block 2 (which includes an eating-behaviour screening question), and three Knowledge files (`nutrition-log.md`, `health-flags.md` in the training skill's format, `current-plan.md`).
- Goals: fat loss while keeping muscle, muscle gain, and endurance, plus combinations. Age and sport modifiers are always loaded.
- Source register with 25 published sources, each read in the original as full text, abstract or legal text. Each entry is marked with how it was read. There are four declared heuristics (H1–H4) for decisions where no primary source gives a number.
- Hard floors: no target below the Mifflin-St Jeor resting energy [Q18] or 1,200 kcal [Q5], weight loss of at most 1 % per week [Q5][Q8], no fasts over 24 h, and no deficit in the 2 weeks before a key race (H3).
- Health-claim guard rails with the official German wording of Regulation (EU) 432/2012 (consolidated 20.08.2025), including the 55+ creatine claim (2017/672) and carbohydrate solutions (2021/686).
- Supplements are tiered and sourced. Vegan users always get a B12 notice [Q11]. Iron is never suggested without a lab value [Q8][Q14]. The skill names the vitamin D upper limit [Q13] and handles user-supplied studies by population, dose, funding and outcome, with no blanket verdicts.
- `check-consistency.py` runs 160 checks. Mutation-tested: a changed carbohydrate range, a table row without a source, a removed disclaimer clause, a wrong worked example, a banned effect word, and an unknown source code are each caught.
