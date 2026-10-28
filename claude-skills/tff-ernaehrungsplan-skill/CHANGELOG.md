# CHANGELOG — TFF Nutrition Plan Skill

Format: append only. Never delete entries.

## Unreleased — ChatGPT edition

- New ChatGPT edition in `chatgpt-skills/tff-nutrition-coach/`: project instructions (6,595 characters) with the safety triage, assessment, hard floors and German disclaimer, plus one reference file built from this skill by `build-reference.py`. A test in the ChatGPT app with the plain skill files skipped the safety questions in one of two chats, used web search and supermarket names, and forecast a weight.
- `project-instructions.txt` (added earlier on this branch line) is removed; the ChatGPT edition replaces it.
- README: "How to use it" points ChatGPT, Gemini and other assistants to the ChatGPT edition. The skill files are unchanged.

## v0.1.4 — 2026-10-28 — Fixes from the blind test on a second model

v0.1.3 was run on a second model (Codex CLI, gpt-6.1-sol) with 10 personas from stages 1 and 2. **9 of 10 were green, no 🛑 criterion was missed**; P8 (ashwagandha claim from a seller) was red (`chatgpt-blindtest/09-bewertung-codex-A/B.md`, `10-zusammenfassung-codex.md`). Fixes, first those that also showed up with Claude:

- Plan step 3: the floor check is written out with numbers — requested kcal vs. floor, requested rate in kg and % per week vs. 1 % — with a German pattern sentence. Until now this was only in the HARD FLOORS text and got lost after the assessment.
- PAL for 1–3 sessions: the TDEE range uses the full occupation band, the energy target starts in its upper half. `sport.md` and SKILL.md no longer contradict each other.
- Pregnancy in the RED-S hold row: ending the deficit does not wait; new kcal or macro numbers wait until a test or a doctor rules pregnancy out. The user's own guess after a missed period does not.
- UPDATE MODE: minimum output for every update, also with a hold (rate from the weekly averages, energy decision, updated Knowledge files, ✓ Notiert).
- Rule 17: kcal per food = 4/4/9 from its macros, values derived from the amount, never adjusted to hit the sum.
- Knowledge templates are binding, with German versions. Columns, 1–5 scales, ISO dates and `Count:` stay unchanged, otherwise the RED-S trigger in UPDATE MODE cannot fire.

Only seen with Codex, closed in the text:

- Under 18: German sentence that always names the parents. Referral rows: German refusal sentence "keinen Ernährungsplan, auch keinen sanften".
- Block 1: no plan promise before Block 2.
- Plan step 3: Mifflin-St Jeor with every intermediate product. Step 8: example days must differ.
- ANALYSIS MODE: disease claims are named first (`claims.md` step 0); the A/B question is fixed, with German wording.
- User-brought studies: numbers from the user's text are restated as "laut deinem Text" (Rule 5 does not apply to them); no recommendation or rejection as the opening; the seller's possible conflict of interest is a mandatory sentence.
- `check-consistency.py`: 200 checks (25 new).

Re-test of P2, P6, P8, P9, P12, P32 on Codex with these fixes: all six green, P8 now green (`11-bewertung-codex-v014-A/B.md`). Polished before release, from that re-test:

- Hold row: "no deficit" is said without a number and points upward ("eat more than during the weight-loss phase, guided by hunger"). "At least as much as before" would have kept the deficit.
- UPDATE MODE: hold signals in the log are asked about (cycle, pregnancy test) before any number. `current-plan.md` is output as a complete replacement file and keeps the old PAL unless work or training changed.
- `sport.md`: energy target = upper half of the TDEE range minus H1, as one range. Sessions longer than 60 min count toward the +0.3 (Codex had dropped it for 4 × 75 min).
- Under 18: shorter German sentence, still naming the parents. German no-plan disclaimer reads "Sie ist keine …".
- `supplements.md`: the ISSN sponsorship note covers creatine, caffeine and protein powder, with a German sentence. `claims.md` step 0: no invitation to look for a study on the disease part.
- UPDATE MODE with a hold: "stop there" in step 3 contradicted the minimum output in step 8, and Codex output no Knowledge files (P32, `12-bewertung-codex-endstand.md`). Now: the first message asks without numbers; the next gives the disclaimer, the rate from the user's own log, the no-deficit sentence and a complete `current-plan.md` whose energy line says "no deficit — new number pending medical clarification", so the old deficit target does not stay in Knowledge.

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
