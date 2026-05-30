---
title: "AI Is Not the Next Internet — It's the Next Railroad"
description: "Why AI's physical infrastructure demands signal an industrial revolution, not just another tech bubble"
published: true
tags: ai, hardware, economics, technology
---

Last week, an economist I know dropped a take that made me stop scrolling.

Normally economists' hot takes on tech are comfortably wrong in predictable ways — they underestimate software's compounding effects, overestimate capital cycles, and talk about productivity like it's a dial you can turn. But this one had a sharper edge.

> Every major technological revolution has come with a transformation in how we use energy. Steam → coal. Internal combustion → oil. Electricity → copper + grid.
>
> The internet and mobile internet did NOT. They ran on existing infrastructure — existing PCs, existing phones, existing fiber. The increment was entirely in software.
>
> AI is different. AI directly consumes energy — electricity for training clusters, rare gases for semiconductor lithography, copper for new grid connections, lithium for the storage that renewable + AI demand requires.
>
> When a "software revolution" starts pulling on the periodic table, something fundamental has shifted. Either it's the biggest bubble in history, or we're at a singularity.

The framework is good. The numbers are off by about 2x. And the conclusion excludes every middle ground. Let me unpack.

## The Signal That's Real

The core observation is correct and underappreciated: AI requires *building* physical infrastructure, not just *using* it.

The internet's physical layer was already in place. 1990s data centers ran on the same grid, same copper, same buildings as 1970s mainframes. The mobile internet ran on phones that were already manufactured. Yes, lithium-ion scaled up because of smartphones — but that was a serendipitous byproduct, not a structural requirement.

AI is structurally different:

| Layer | What AI Needs | What That Pulls On |
|-------|--------------|-------------------|
| **Training clusters** | New GPU factories | Silicon, rare gases (lithography), copper (packaging), cooling fluids |
| **Inference at scale** | Grid capacity expansion | Transformers, copper cable, switchgear, natural gas/nuclear for baseload |
| **Energy storage** | Renewable intermittency backup | Lithium, cobalt, nickel, graphite — at battery-grade volumes |
| **Data centers** | New buildings | Steel, cement, land, water (for cooling) |

This is a supply-chain-level reconfiguration, not a software upgrade. The internet changed how bits flow. AI changes how atoms are allocated.

## Where the Argument Overshoots

**"The internet had no energy impact"** — This understates mobile's role in scaling lithium-ion from laptop-grade (~50Wh cells) to a 10-billion-unit industry that directly enabled Tesla's battery supply chain. The energy shift happened; it was just already absorbed into the smartphone's success before AI came along to amplify it.

**"The whole periodic table is rising"** — No. Copper is up (grid + data center wiring). Lithium is volatile (storage, already cyclical). Silver is up modestly (solar + high-conductivity connections). But hafnium, rhenium, antimony, gallium — the elements AI *doesn't* feed on — are flat. "All elements" is rhetorical, not factual.

**"Either the biggest bubble or singularity"** — This is the weakest part, and it's a classic false dichotomy. Between a bubble that destroys all value and a singularity that ends history lies a vast, well-documented middle: normally transformative technological revolutions.

| Revolution | Energy/Materials Impact | Outcome |
|-----------|----------------------|---------|
| Railroads (1830s) | Coal + steel boom | Bubble burst, railroads stayed. Transformed economic geography. |
| Electricity (1890s) | Copper + coal boom | Bubble burst, grid stayed. Transformed daily life. |
| Internet (1990s) | Fiber boom | Bubble burst, internet stayed. Transformed information access. |
| AI (2020s) | Copper + electricity + rare gases | Most likely: bubble partially deflates, AI stays. Transforms ??? |

Every single one of these was called "either the biggest bubble or the end of the world" by contemporaries. Every single one landed in the middle.

## The Unspoken Assumption

The argument's biggest hole is that AI's energy consumption is a *hard constraint* — a physical necessity that will grow unboundedly regardless of efficiency.

That's false on three levels:

1. **Inference optimization is compounding at ~2x/18 months.** Quantization, distillation, speculative decoding, MoE routing — every generation of inference engine cuts energy per token by roughly half. This largely offsets demand growth.

2. **Chip efficiency per generation: H100 → B200 → Rubin.** Each generation improves performance-per-watt by 2-3x. Training the same model in 2028 will use significantly less energy than today.

3. **Renewable energy costs are still falling.** Solar + wind + battery storage costs have been dropping ~10-15%/year for a decade. The energy AI consumes will increasingly be the cheapest energy.

AI will consume more electricity. But it's a gradual demand-side pressure, not a sudden new industrial sector appearing overnight.

## What This Actually Means

The economist's hot take identifies a real phenomenon — AI's physical intensity is higher than the internet's — and correctly uses that to argue this isn't "just software." But it overshoots on magnitude and truncates the outcome space.

The most accurate framing:

> **AI is a 19th-century-railroad-level technological shift.** It requires massive physical infrastructure buildout, pulls on energy and materials, and will reshape economic geography. But it is neither a bubble (the technology has real value) nor a singularity (running out of copper won't produce AGI). It lands in the normal revolutionary middle.

For practitioners, this has two implications:

1. **Physical supply chains matter now.** If you work on energy, materials, or chips, the demand signal is structural, not cyclical. Copper grid connections, transformer manufacturing, and rare gas supply chains will be tight for a decade.

2. **Don't choose between "bubble" and "singularity."** Both are unhelpful frames. The useful question is: *Can the productivity gains from AI pay for the physical infrastructure it requires?* If yes, this is a normal, healthy industrial upgrade. If no, we get a correction — and the technology survives with more efficient allocation.

That's a much harder question than "bubble or singularity." And it's the one worth answering.

---

*Using this? A ⭐ or a one-word issue tells me what to build next — helps more than you'd think.*
