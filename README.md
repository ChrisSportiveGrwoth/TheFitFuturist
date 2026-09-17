# TheFitFuturist — AI Training Skills

Open-source skills for AI training assistants, built and tested by
[TheFitFuturist](https://www.thefitfuturist.com).

Each skill is a ready-to-use ZIP you upload to the assistant it was built for.
Done in about two minutes.

## About TheFitFuturist

TheFitFuturist explores the intersection of AI and training science —
not by reviewing apps, but by building tools, testing prompts, and
sharing what actually works.

The skills in this repo are the result of iterative development and
empirical testing: each skill is evaluated against structured test
personas with defined scoring rubrics before release. Not perfect —
but tested.

→ [thefitfuturist.com](https://www.thefitfuturist.com)
→ [Substack](https://thefitfuturist.substack.com)
→ [X / Twitter](https://twitter.com/TheFitFuturist)

## Available Skills

### [TFF Training Plan Skill — for Claude](./claude-skills/tff-trainingsplan-skill/)
Personalized training plans for runners, strength athletes, and mixed goals.
Tested against 41 personas across running, strength, and mixed training.
Install via Claude → Settings → Customize → Skills.
→ [Latest release and download](https://github.com/ChrisSportiveGrwoth/TheFitFuturist/releases/latest)

### [TFF Training Coach — for ChatGPT](./chatgpt-skills/tff-training-coach/)
The same sports-science core, packaged for ChatGPT's skill format. Install via
ChatGPT → Plugins → Skills → Create → Upload from your computer.

Two things to know before you download it: OpenAI currently documents skills for
Business, Enterprise, Healthcare and Edu accounts, so the upload path may not exist
on a personal plan — the skill's README explains how to check and what to use
instead. And the edition carries a small set of deliberate changes against the
Claude version, all listed in
[DEVIATIONS.md](./chatgpt-skills/tff-training-coach/DEVIATIONS.md), which have not
yet been re-run against the 41-persona suite.

→ [Read the full development story on Substack](https://thefitfuturist.substack.com)

## Important Disclaimer

**Use all skills, tools, and outputs from this repository at your own risk.**

- Skills are instruction sets for AI language models (Claude by Anthropic,
  ChatGPT by OpenAI). They do not guarantee consistent, identical, or error-free
  output —
  LLMs are probabilistic by nature and results will vary between runs,
  model versions, and contexts.
- Nothing in this repository constitutes medical, health, or professional
  coaching advice. Always consult a qualified professional before starting
  any training program.
- TheFitFuturist and Sportive Growth Ltd. accept no liability for any
  injury, health issue, or other damage arising from the use of these
  skills or the plans they generate.
- Scores and benchmark results reflect performance under specific test
  conditions and do not guarantee equivalent results in real-world use.

## License
© 2026 TheFitFuturist — Sportive Growth Ltd.
Licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) —
free for personal use and adaptation, not for commercial use without permission.
