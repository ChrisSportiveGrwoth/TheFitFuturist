---
author: TheFitFuturist | https://www.thefitfuturist.com
license: CC BY-NC 4.0
---

# Goal: Fat Loss While Keeping Muscle

## How to use this file

Principles, not templates. The goal is *high-quality* weight loss: losing fat while keeping fat-free mass [Q5]. The HARD FLOORS in SKILL.md apply on top of everything here. Combined with endurance, also load `endurance.md` — see Principle 6.

---

## Principle 1: Rate decides, calories follow

- Target rate: **0.5–1.0 % of body weight per week**, upper limit 1 % [Q5][Q8].
- Starting energy: estimated TDEE minus **300–500 kcal/day** (H1) — a starting value, corrected by the 7-day average weight after 2 weeks.
- Check the start against the floors: never below the user's estimated resting energy expenditure (Mifflin-St Jeor [Q18]) and never below 1,200 kcal [Q5]. If TDEE minus 300 already hits a floor, the deficit is the distance to the floor — and the rate will be slower. Say so instead of breaking the floor.
- Very low energy diets (< 800 kcal) and low energy diets (800–1,200 kcal) give faster short-term loss but no long-term advantage over moderate restriction, may increase lean mass loss and are unsuitable for lean people [Q5]. They are not offered.

**Show the user the rate in kg** for their weight: 80 kg × 0.5–1.0 % = 0.4–0.8 kg/week. Never as a promise (claims rules), always as "realistic range". **Never convert it into a time to reach the goal** (no "X kg in Y Wochen", HCVO Art. 12 b [Q7]) — name a checkpoint date instead.

## Principle 2: Protein — the main lever for keeping muscle

| Situation | Range | Source |
|---|---|---|
| No strength training | 1.2–1.6 g/kg/day | [Q5] Statement 6 |
| With strength training | 1.6–2.2 g/kg/day | [Q5] Statement 7 |
| Lean, experienced, resistance-trained, in a sustained deficit | up to 1.9–3.2 g/kg/day; the upper end applies to lean, resistance-trained people only, not to higher body fat or untrained people | [Q5] Statement 7, §5.1 |

**Default:** use the first two rows. Use the third only when the user is clearly lean (measured body fat, physique sport, long training history) — and still start in its lower half (conservative default).

**Which body weight:** the ranges are per kg of body weight in the cited studies, which mostly involve non-obese trained people [Q5]. For BMI ≥ 30, calculate protein from the weight that corresponds to BMI 25 at the user's height (H4) and say that this is the skill's choice.

**Distribution:** total daily protein comes first; the per-meal values are orientation and never override the user's meal rhythm from Block 5 — add a snack only if the user agrees. At least **3 protein-rich meals** per day for active people in a deficit [Q5] Statement 4; per meal ~0.25 g/kg or 20–40 g high-quality protein, every 3–4 h [Q1]. Total daily protein matters most; distribution is secondary [Q5] Statement 5.

## Principle 3: Carbohydrate and fat — by preference

- With protein and energy equal, low-carbohydrate and low-fat diets give similar fat loss [Q5] Statement 8 → split the remaining energy by the user's preference and training.
- Ketogenic diets may give a modest early advantage that fades and may be accompanied by greater lean mass loss [Q5] §5.4 → an option if the user insists, never the recommendation. Not for endurance athletes in hard training (see `endurance.md`).
- **Fat floor:** do not plan chronic fat intakes below 20 % of energy [Q8]; typical 20–35 % [Q8].
- Training days may carry more carbohydrate than rest days if the user trains hard; for strength-only users this is optional — the skill's own choice, no source code.

## Principle 4: Strength training is part of the plan's logic

Resistance training and sufficient protein are *"indispensable mitigators of lean mass loss in a sustained caloric deficit, regardless of the diet type"* [Q5] Statement 5. If the user does no strength training: recommend it once, with this reason, then proceed either way (the skill does not write training plans).

## Principle 5: Diet forms

- **Intermittent fasting** (time-restricted eating, alternate-day, 5:2) shows no different effect from continuous restriction [Q5] Statement 3 → fine if it suits the user's day. No fasting window longer than 24 h (HARD FLOORS).
- **Meal frequency** by preference [Q5] Statement 4, with the 3-protein-meals minimum above.
- **Recomposition** (losing fat and gaining muscle at the same time) is possible, more likely with high protein in resistance-trained people [Q5] §5.1, and less likely the leaner and more advanced someone is. Treat it as a possible side effect, not as the plan's promise. If the user wants it explicitly: maintenance to small deficit, protein in the upper half of the strength row, progressive strength training.

## Principle 6: Combined with endurance

Load `endurance.md` as well.
- Deficit on easy and rest days only; long and hard sessions are fuelled in full (`endurance.md` tables).
- Rate at the lower end (0.5 %/week). Faster loss is more likely to cost performance [Q8].
- No deficit in the final 2 weeks before a key race or in the highest-load block; if the user does not know when that block is, keep the final 5 weeks deficit-free (H3); weight loss belongs in the base phase or well away from competition [Q8].

## Principle 7: Calibration

- Weigh every morning under the same conditions; decisions use **7-day averages** only.
- First check after 14 days. Then the UPDATE MODE pattern table in SKILL.md.
- Adherence before calories: if the plan is not followed, change practicality first.
- Plateau with adherence: one step (H1), never below a floor. If the floor is reached, offer a maintenance phase instead of a further cut.

## Red flags in this goal

| Signal | Action |
|---|---|
| Rate faster than 1 %/week for 2 weeks | Raise energy one step (H1). |
| Hunger 5 + energy 1 over several days, falling performance, missed period | SAFETY TRIAGE hold row (RED-S) — no further deficit. |
| User asks for a lower target than the floor | HARD STOP per SKILL.md, alternatives. |
| Signs of compensatory behaviour in the log ("skipped dinner because I ate cake") | SAFETY TRIAGE referral row — gently. |
