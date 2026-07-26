---
author: TheFitFuturist | https://www.thefitfuturist.com
license: CC BY-NC 4.0
---

# Goal: Running / Endurance

## How to use this file

Running is not one goal — it is a spectrum. A 5k runner and a marathon runner need fundamentally different training. Always identify the user's primary running distance or format before applying any principle.

**First question before planning:** What distance/format did the user state?
- 5k / 10k → VO2max and speed focus, moderate volume
- Half Marathon → balance of aerobic base and quality work
- Marathon → high volume, aerobic base dominates
- Trail / Ultra → extreme volume, elevation-specific work, strength critical
- General fitness → health and consistency, no performance target

Then: derive intensity distribution, periodization, and session types from the distance-specific principles below. Strength training is strongly recommended for every runner type — integrate it using the sequencing rules in Principle 5. The user is offered an explicit opt-out in Block 5 of the assessment; if they decline, respect that answer and follow the single-line note rule in SKILL.md instead of arguing the point through the plan.

---

## Principle 1: Training Intensity Distribution (TID) by Distance

**The principle:**
The optimal intensity distribution is not fixed — it depends on the target distance. Shorter distances demand more high-intensity work. Longer distances demand more aerobic base volume.

**5k / 10k:**
- Energy system: primarily aerobic with significant anaerobic contribution
- TID: Pyramidal → ~70% Z1-2, ~20% Z3, ~10% Z4-5
- Key sessions: VO2max intervals (Z4-5), tempo runs (Z3), easy runs
- Volume: moderate (30-60 km/week for intermediate)
- Reasoning: VO2max is the primary performance limiter at these distances

**Half Marathon:**
- Energy system: predominantly aerobic, threshold capacity critical
- TID: Pyramidal or POL → ~75-80% Z1-2, ~10-15% Z3, ~5-10% Z4-5
- Key sessions: long run, tempo/threshold runs, occasional intervals
- Volume: moderate-high (40-70 km/week for intermediate)
- Reasoning: lactate threshold pace determines race performance

**Marathon:**
- Energy system: almost entirely aerobic (fat oxidation + glycogen)
- TID: POL or Pyramidal → ~80-85% Z1-2, ~5-10% Z3, ~5% Z4-5
- Key sessions: long run (primary), marathon-pace runs, easy runs dominate
- Volume: high (50-80+ km/week for competitive amateurs)
- Reasoning: aerobic base and fat oxidation efficiency are the primary limiters

**Trail / Ultra:**
- Energy system: aerobic base + muscular endurance + elevation-specific work
- TID: ~85-90% Z1-2, minimal Z3-5
- Key sessions: long run with elevation, back-to-back long runs, hiking counts
- Volume: very high, time-based rather than distance-based
- Reasoning: time on feet and elevation gain matter more than pace

**General fitness running:**
- No performance target — health, enjoyment, consistency
- TID: 100% Z1-2, no high-intensity work unless user requests it
- Volume: what the user can sustain without injury or burnout
- Reasoning: adherence is the only metric that matters here

**Important nuance:**
Neither POL nor Pyramidal is universally superior. POL shows advantages for trained athletes and shorter interventions. Pyramidal is effective for recreational runners and those building volume. Select based on user's training history and goals — do not default to "80/20 always."

---

## Principle 2: Periodization by Distance

**The principle:**
Structure depends on whether there is a target event and which distance.

**Without a target event:**
- Simple 3+1 block: 3 weeks progressive loading → 1 deload week (-30-40% volume)
- Beginners: build consistency first, no periodization needed

**With a target event:**
Calculate available weeks from today to event date, then:

| Phase | % of total weeks | Focus |
|---|---|---|
| Base | 40% | Volume, Z1-2 only, build aerobic engine |
| Build | 35% | Introduce quality sessions, increase volume |
| Peak | 15% | Reduce volume, sharpen race-specific intensity |
| Taper | 10% | Drastically reduce volume, keep some intensity |

**Distance-specific taper length:**
- 5k/10k: 1-2 weeks taper
- Half Marathon: 2 weeks
- Marathon: 2-3 weeks
- Ultra: 2-3 weeks (but less intensity reduction — keep legs moving)

**Renormalization for plans under 20 weeks — apply this, do not use the percentages directly:**

The percentage split above describes the shape of a long build-up. Taken literally it only works from 20 weeks upward: a 10 % taper on a 12-week plan is 1.2 weeks, which contradicts the distance-specific taper lengths right below it. For anything shorter, allocate in this order:

1. **Taper first, in absolute weeks** from the distance-specific list above (5k/10k 1 | HM 2 | Marathon 2 | Ultra 2). Cap it at 25 % of the plan — a 6-week plan does not get a 2-week taper; use 1 week.
2. **Peak** = 15 % of total, rounded to whole weeks, minimum 1, maximum 3.
3. **Split the remainder** between Base and Build at roughly 55 / 45 in favour of Base.
4. **Round to whole weeks**, give any leftover week to Base, and name every phase in the plan.

Worked examples: 12-week marathon → Base 4 / Build 4 / Peak 2 / Taper 2. 8-week 10k → Base 3 / Build 3 / Peak 1 / Taper 1. 16-week half → Base 7 / Build 5 / Peak 2 / Taper 2.

If the resulting Base phase is shorter than 3 weeks, the plan is too short for the distance — check it against the minimum preparation table in SKILL.md before continuing.

**Volume progression rule:**
Never increase total weekly volume by more than 10% per week. Never increase volume AND intensity in the same week.

---

## Principle 2b: Pace Estimation (when user doesn't know their times)

**The principle:**
If a user doesn't know their current pace or race times, estimate from fitness level and target distance. Always state this is an estimate and adjust based on first sessions.

**Estimation table:**

| Fitness level | Easy pace (Z2) | 5k estimate | 10k estimate | Half estimate |
|---|---|---|---|---|
| Beginner | 8:00-10:00/km | 40-55 min | 85-115 min | 3:00-4:00h |
| Intermediate | 6:00-7:30/km | 30-40 min | 62-85 min | 2:15-3:00h |
| Advanced | 4:30-6:00/km | 20-30 min | 42-62 min | 1:35-2:15h |

These values are the single source together with `assessment.json` → `pace_estimation_when_unknown`; both must always say the same thing. Never estimate slower than the per-level `max_easy_pace_cap` (Beginner 10:00/km | Intermediate 7:30/km | Advanced 6:00/km).

**Beginner caveat:** at this level easy pace and race pace converge — a beginner running 5k in 50 min is at 10:00/km in the race, so there is no meaningfully slower "easy" gear left. When the estimate approaches the 10:00/km cap, plan walk-run intervals instead of continuous easy runs, and set the running segments by time, not by pace.

Always state in the plan: "Estimated easy pace: ~X min/km based on your fitness level. Adjust after your first session — if it feels too easy or too hard, report back and I'll recalibrate."

---

## Principle 2c: From a Known Race Time to Target Pace and Training Paces

**The principle:**
When the user states a recent race time, do not fall back on the fitness-level table — derive everything from that result. This is the most common case for anyone with a training history, and without it the plan has no pace anchors.

**Step 1 — Equivalent time at another distance (Riegel):**

`T2 = T1 × (D2 / D1)^1.06`

Worked example: 10 km in 48:00 → half marathon = 48 × (21.1 / 10)^1.06 ≈ 106 min ≈ 1:46.

Honest limits — state them when you use it: the exponent 1.06 is a population average, individual endurance varies. The formula is reliable when the two distances are within roughly a factor of two of each other and the runner has the endurance base for the longer distance. Extrapolating 5k → marathon systematically predicts times that are too fast for runners without marathon-specific volume. For the marathon, treat the Riegel result as a ceiling, not a target.

**Step 2 — Sanity-check the user's goal time** against the Riegel equivalent. If the goal is more than ~5 % faster than the equivalent, apply the "Goal pace >30 % faster" and "ambitious goal" validation rules in SKILL.md — flag it once, plan against the more conservative pace, and say so.

**Step 3 — Derive training paces from race pace.** Anchor everything on the current 10k race pace (measured or Riegel-derived):

| Training pace | Derivation | Use |
|---|---|---|
| Easy / Z2 | 10k pace + 75–105 s/km | Most of the weekly volume |
| Long run | 10k pace + 75–120 s/km, slower end as distance grows | Long run |
| Marathon pace | 10k pace + 25–40 s/km | Marathon-specific work |
| Threshold / tempo (Z3-4) | 10k pace + 10–20 s/km — roughly the pace holdable for one hour | Tempo and threshold sessions |
| Interval / VO2max (Z5) | 10k pace − 10–15 s/km, i.e. around 5k pace | 3–5 min intervals |
| Strides / neuromuscular | Clearly faster than 5k pace, controlled, 20–30 s | End of easy runs |

These offsets are approximations that hold for recreational runners; they widen for slower runners and compress for fast ones. Always present them alongside the HR zones, state that the ranges are derived from the stated race time, and tell the user to correct them after the first two weeks based on feel and HR.

**Step 4 — Fill the pace column of the HR zone table (Principle 6) from this table.** Zones and paces must be shown together — a bpm range alone is not executable, and pace alone ignores day-to-day condition.

---

## Principle 3: Session Types, Purpose and Introduction Timing

Build the weekly plan from these blocks — assign based on distance priority, not arbitrary days.

| Session type | Purpose | Intensity | Distance relevance |
|---|---|---|---|
| Long run | Aerobic base, fat oxidation | Z1-2 | All — most important for marathon/ultra |
| Easy run | Recovery, aerobic maintenance | Z1 | All — fills non-key days |
| Strides | Running economy, neuromuscular activation | Z4-5, 20-30 sec only | ALL distances — introduce from week 3-4 |
| Tempo / threshold | Lactate threshold development | Z3-4 | Half marathon / marathon primary |
| VO2max intervals | Maximal aerobic capacity | Z4-5 | 5k/10k primary |
| Hill repeats | Running economy, strength | Z3-5 | Trail primary, benefits all |
| Strength | Injury prevention, economy | N/A | If user opted in — see Principle 5 |

**Distance-specific intensity progression — CRITICAL FOR 5k/10k:**

5k/10k goal requires VO2max development. **MANDATORY: Z4-5 intervals MUST start by Week 4 at the latest for 5k/10k goals.** Do NOT stay in Z1-2 only beyond week 3.

| Phase | 5k/10k | Half Marathon | Marathon |
|---|---|---|---|
| Base (weeks 1-3) | Z1-2 + strides from week 3 | Z1-2 only | Z1-2 only |
| Early build (weeks 4-6) | Z3 tempo + Z4 intervals begin | Z3 tempo begins | Z1-2 + strides |
| Build (weeks 7-9) | Z4-5 intervals 1x/week | Z3-4 threshold | Z3 tempo begins |
| Peak (weeks 10-11) | Z4-5 intervals + race pace | Z4 threshold | Z3-4 threshold |
| Taper | Volume down, keep some Z4 | Volume down, keep Z3 | Volume down |

**Strides — introduce for ALL distances from week 3-4:**
- 4-6 × 20-30 sec at Z4-5 effort with full recovery (90 sec walk)
- Done at END of easy run — not as a separate session
- No equipment needed, low knee stress, high economy benefit
- Do NOT skip strides — they are the lowest-cost, highest-return quality work

**Planning logic:**
1. Assign key sessions first (non-negotiable based on distance goal)
2. Never place two hard sessions on consecutive days
3. Fill remaining days with easy runs or rest
4. Specific days derive from this logic, not from a fixed template
5. For 5k/10k: if plan stays in Z1-2 beyond week 4, flag it — the goal requires intensity

---

## Principle 4: Recovery Times

| Session | Minimum before next hard session |
|---|---|
| Long run (>60 min) | 48h |
| Tempo / threshold run | 48h |
| Intervals / high-intensity | 48h |
| Easy run | No restriction |
| Leg strength (heavy) | 48h before key run |

**Hard/Easy principle:** Every hard session must be followed by at least one easy day. Flag any plan that places two hard sessions back-to-back.

---

## Principle 5: Strength & Plyometric Training (Strongly Recommended for All Runner Types)

**The principle:**
Strength training and plyometric training both improve running economy. Combined is most effective. Heavy, low-rep strength (≥80% 1RM) improves economy primarily at higher speeds. Plyometrics improve economy at lower speeds (≤12 km/h). For most recreational runners, a combination session works best.

**Important honest caveat on injury prevention:**
Evidence that strength training prevents running injuries is inconclusive in unsupervised settings. Supervised programs show significant reduction (~30%). Hip and core strengthening shows the clearest injury prevention signal. Do not oversell strength training as a guaranteed injury shield — frame it as running economy improvement with a likely injury reduction benefit.

**Strength approach by distance:**

| Distance | Strength focus | Load | Frequency |
|---|---|---|---|
| 5k / 10k | Heavy compound + plyometrics | ≥80% 1RM | 2x/week |
| Half Marathon | Heavy compound + plyometrics | 75-85% 1RM | 1-2x/week |
| Marathon | Lower load, plyometrics | 60-75% 1RM | 1-2x/week |
| Trail / Ultra | Single-leg stability + hill-specific | Moderate | 2x/week |
| General fitness | Moderate load, full body | 60-75% 1RM | 1-2x/week |

**Priority exercises by equipment:**

Full gym:
- Bulgarian split squat, RDL, hip thrust, eccentric calf raise, Nordic curl

Home gym (dumbbells):
- DB split squat, DB RDL, glute bridge, eccentric calf raise, Nordic curl (use couch/sofa to anchor feet)

Bodyweight only:
- Pistol squat progressions, single-leg glute bridge, step-up, Nordic curl (anchor feet under sofa), eccentric calf raise (single leg on step), dead bug, pallof press with band
- Nordic curl is achievable bodyweight — anchor feet under sofa, lower slowly (3-4 sec), push up with hands

Outdoor only:
- Hill repeats substitute for gym strength, bodyweight circuit above, eccentric calf on curb/step

**Minimum Exercise Anchors — required in every running plan (all sessions combined):**
- **Eccentric lower-leg:** Single-leg calf raise with 3s lowering — essential for Achilles and knee health
- **Posterior chain:** Nordic curl / sofa curl or RDL — hamstring injury prevention, strong evidence base
- **Hip stability:** Clamshell or side-lying abduction — knee stability, most critical for knee issues
- Glute bridge / hip thrust — hip extension power for running economy

**Plyometric component (add for intermediate+):**
- Calf hops / ankle stiffness drills — improve leg spring stiffness
- Hurdle hops / box jumps — power and ground contact time
- Strides — see Principle 3
- Beginners: skip plyometrics until 6+ months of consistent running

**Sequencing rule:**
Never place leg strength or plyometric session within 24h before a key run. Ideal placement: after an easy run or rest day.

---

## Principle 5b: Wearable Data Integration

**If user uploads wearable data (CSV or screenshot):**

Always reference it explicitly in the plan. Examples:
- "Based on your Garmin data, your average easy run pace over the last 4 weeks was X min/km — I'll use this as baseline."
- "Your Polar data shows average HR of X bpm on easy runs — this maps to your Z2, confirming your aerobic base."
- "Your WHOOP recovery scores averaged X% over the last 4 weeks — I'll schedule hard sessions on days with recovery >70%."
- "Your Oura HRV trend shows a drop last week — this confirms the deload timing."

**If no wearable data:** use assessment answers only.

**Device-specific data points to look for:**
- Garmin: pace, HR, training load, VO2max estimate, recovery time
- Polar: HR zones, training load, orthostatic test (HRV proxy)
- WHOOP: recovery score, strain, HRV, sleep performance
- Oura: readiness score, HRV, sleep stages
- Apple Watch: workout HR, active calories (less useful for training zones)

---

## Principle 6: Heart Rate Zones — Always Output in Plan

**MANDATORY:** Every running plan must include the user's personal HR zones with actual bpm values.

**Calculation hierarchy:**
1. Lab test (spiroergometry / lactate) → use those values directly, most accurate
2. Field test (20-min max HR test) → use average HR last 10 min as lactate threshold HR
3. Device estimate → use but flag: "These are device estimates and may be off by 10-20 bpm. Consider a field test for more precision."
4. Age-based only → calculate with Tanaka (208 − 0.7 × age), flag as approximation

**Karvonen formula (when resting HR is known):**
- HR Reserve = Max HR - Resting HR
- Zone bpm = Resting HR + (% × HR Reserve)

**Age-based formula (when resting HR unknown):**
- Max HR = 208 − (0.7 × age) — Tanaka et al. 2001, JACC (meta-analysis, 351 studies / >18,000 subjects)
- More accurate than the older 220-age rule, which overestimates Max HR in younger adults and underestimates it with increasing age (~10 bpm difference by age 70)
- Zones as % of Max HR

**⚠️ The percentage column must name the method it belongs to. The two systems are not interchangeable:**

- Karvonen → the percentages are **% of heart rate reserve (% HRR)**. Header: `% HRR (Karvonen)`.
- Age-based → the percentages are **% of maximum HR (% max HR)**. Header: `% max HR`.

The same number produces different bpm. Age 42, resting HR 58, Tanaka max HR 179: Z2 at 60–70 % HRR = 130–142 bpm; 60–70 % of max HR = 107–125 bpm. That is a 23 bpm gap — a full zone. Never put a "% max HR" label on Karvonen-derived bpm values, and never let the user carry the percentages over into a device that uses the other method. The bpm values are the deliverable; the percentages only document how they were derived.

**Always show this table in the plan — use the header row matching the method actually used:**

| Zone | Name | % HRR (Karvonen) *or* % max HR | bpm (calculated) | Pace (min/km) | Feel |
|---|---|---|---|---|---|
| Z1 | Recovery | 50-60% | XX-XX bpm | X:XX-X:XX | Fully conversational |
| Z2 | Aerobic base | 60-70% | XX-XX bpm | X:XX-X:XX | Easy, can hold conversation |
| Z3 | Aerobic endurance | 70-80% | XX-XX bpm | X:XX-X:XX | Harder, short sentences |
| Z4 | Threshold | 80-90% | XX-XX bpm | X:XX-X:XX | Hard, can't talk much |
| Z5 | VO2max | 90-100% | XX-XX bpm | X:XX-X:XX | Maximum, unsustainable |

Replace XX-XX with actual calculated values. Fill the pace column from Principle 2c (race time known) or Principle 2b (estimated). State which formula was used, and add: *"The bpm values are what counts — enter those into your watch. If your device asks for percentages, check whether it works from max HR or from heart rate reserve; the same percentage means different things in each."*

---

## Principle 7: Mobility, Flexibility & Cross-Training

**Mobility and flexibility — honest evidence base:**
Static stretching before running does not reduce injury risk and may temporarily reduce force production. Dynamic warm-up (leg swings, hip circles, walking lunges) is more appropriate pre-run. Post-run static stretching is acceptable for perceived recovery but has limited injury prevention evidence.

**What does have evidence:**
- Gait retraining (e.g. increasing cadence, reducing overstriding) reduces injury risk
- Hip abductor and glute strength reduces knee injury risk
- Foot and ankle strengthening reduces lower leg injury risk

**Practical mobility approach:**
- Pre-run: 5-10 min dynamic warm-up (hip circles, leg swings, calf raises, light strides)
- Post-run: gentle static stretching if desired (calves, hip flexors, hamstrings) — not mandatory
- Dedicated mobility sessions: only if user has specific tightness or injury history — not for everyone

**Cross-training (include when relevant):**
Cross-training reduces running volume while maintaining aerobic fitness during injury or recovery:
- Cycling: minimal leg muscle damage, excellent aerobic stimulus, best cross-training option for runners
- Swimming: full body, no impact, good for injury periods
- Aqua jogging: maintains running-specific fitness, use when injured but not as primary training

Recommend cross-training when: injury risk is high, user is coming back from injury, or training load needs to be reduced but aerobic base must be maintained.

---

## Principle 8: Red Flags

**When these actions apply:** the overuse rows below take effect on the **second report of the same complaint, or on the first report if the user describes it as persistent, worsening, or present at rest** — this matches the count logic in SKILL.md UPDATE MODE, where a single, mild, first-time complaint is logged rather than acted on. The **emergency row is different: it acts immediately, on the first mention, regardless of count**, and is part of the SAFETY TRIAGE list in SKILL.md.

| Signal | Reasoning | Action | Trigger |
|---|---|---|---|
| Knee pain during/after runs | Possible IT band, patellar overuse | Reduce volume 50%, no downhill, add hip abductor work | 2nd report, or 1st if persistent/worsening |
| Shin pain | Possible shin splints | Reduce to 2x/week, add calf work, check footwear | 2nd report, or 1st if persistent/worsening |
| Achilles/calf tightness | Tendon overload | Add eccentric calf work, reduce volume, no speedwork | 2nd report, or 1st if persistent/worsening |
| Persistent fatigue >5 days | Overtraining or illness | Immediate deload week | Immediately |
| Chest pain, dizziness, fainting, palpitations, disproportionate breathlessness | Possible cardiac event | Stop all training, refer to doctor immediately; emergency services if at rest or with arm/jaw pain, sweating or nausea | ⚠️ Immediately, first mention, no exceptions |
| Calf pain with swelling, warmth or redness | Possible thrombosis | Stop training, same-day medical assessment | ⚠️ Immediately, first mention |

---

*Built by [TheFitFuturist](https://www.thefitfuturist.com) — License: CC BY-NC 4.0*
