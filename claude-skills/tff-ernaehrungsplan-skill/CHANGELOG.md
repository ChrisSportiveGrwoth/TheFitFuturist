# CHANGELOG — TFF Nutrition Plan Skill

Format: append only. Never delete entries.

## v0.1.0 — 2026-10-27 — First version, in validation

Not released. Built from the spec in the TheFitFuturist editorial repo. It was written in parallel to the article *KI-Ernährungsplan erstellen* (thefitfuturist.com/training-analyse/ki-ernaehrungsplan-erstellen/).

- Structure mirrors the TFF Training Plan Skill v2.5.5. It has 18 mandatory rules, a safety triage above all modes, a 6-block assessment with a non-skippable Block 2 (which includes an eating-behaviour screening question), and three Knowledge files (`nutrition-log.md`, `health-flags.md` in the training skill's format, `current-plan.md`).
- Goals: fat loss while keeping muscle, muscle gain, and endurance, plus combinations. Age and sport modifiers are always loaded.
- Source register with 25 published sources, each read in the original as full text, abstract or legal text. Each entry is marked with how it was read. There are four declared heuristics (H1–H4) for decisions where no primary source gives a number.
- Hard floors: no target below the Mifflin-St Jeor resting energy [Q18] or 1,200 kcal [Q5], weight loss of at most 1 % per week [Q5][Q8], no fasts over 24 h, and no deficit in the 2 weeks before a key race (H3).
- Health-claim guard rails with the official German wording of Regulation (EU) 432/2012 (consolidated 20.08.2025), including the 55+ creatine claim (2017/672) and carbohydrate solutions (2021/686).
- Supplements are tiered and sourced. Vegan users always get a B12 notice [Q11]. Iron is never suggested without a lab value [Q8][Q14]. The skill names the vitamin D upper limit [Q13] and handles user-supplied studies by population, dose, funding and outcome, with no blanket verdicts.
- `check-consistency.py` runs 160 checks. Mutation-tested: a changed carbohydrate range, a table row without a source, a removed disclaimer clause, a wrong worked example, a banned effect word, and an unknown source code are each caught.
