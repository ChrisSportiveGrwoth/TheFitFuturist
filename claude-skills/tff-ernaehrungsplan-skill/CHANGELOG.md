# CHANGELOG — TFF Nutrition Plan Skill

Format: append only. Never delete entries.

## v0.1.3 — 2026-10-27 — Fixes from validation stage 2

Stage 2 tested 24 more personas on v0.1.2: goal × age, goal × sport, endurance special cases, diet forms, gates, referrals, claims, mixed language, race in 2 days, UPDATE MODE and an injection via a training-plan file. **All 24 were green and none failed** (`07-bewertung-s2-A/B/C.md`). Fixes for the findings that came from the skill text:

- RED-S hold row: a missed period can also mean pregnancy. The skill names this and gives no new numbers until it is clarified. In UPDATE MODE, the hold ends the deficit and raises energy to at least maintenance; this overrides the one-step rule.
- Plan step 3: the PAL range stays inside one DGE band. No uncoded "uncertainty" range.
- `endurance.md`: the fat share is checked per day type (20–35 %), not only as a weekly average. The interval between gel portions is marked as the skill's practical suggestion.
- `fat-loss.md` + endurance: in the deficit phase, key and long session days keep the maintenance carbohydrate values.
- `claims.md`: every condition of an approved claim is kept, spelled out for creatine 55+.
- Rule 12: the language stays consistent, including N labels, H sentences and Knowledge file headings.
- `current-plan.md` template: occupation and typical session duration, so UPDATE MODE does not have to guess.

## v0.1.2 — 2026-10-27 — Fixes from the re-run on v0.1.1

The re-run of P6, P8, P10 and P11 on v0.1.1 left all four personas green with no ❌ (`03-bewertung-run2.md`). Fixes for the skill-text findings:

- Rule 3: a HARD STOP is the one exception to "calculate nothing aloud". It shows the disclaimer first, then only the numbers it needs.
- Rule 17: the 5 % limit applies to all four values (kcal, protein, carbohydrate, fat), not only to kcal.
- `sport.md`: walking or cycling to work does not move an office job into a higher PAL band. When the description fits two bands, the lower one applies.
- `fat-loss.md`: when the deficit sits only on easy days, H1 applies to the weekly average.
- `muscle-gain.md`: no safety statement attached to [Q3].
- `current-plan.md` template: new Phases field for plans that change over time.
- Block 1: the skill asks for a date or event if the user did not name one.

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
