---
name: simonian-computational-global-macro
description: "Knowledge base from \"Computational Global Macro: Game Theory, Machine Learning, and Causal Inference\" by Joseph Simonian. Use when applying Simonian's frameworks for geopolitical risk analysis, game-theoretic simulation with bandits and Q-learning, causal inference and Noisy-OR models, causal-view portfolio construction, and judgment aggregation, studying the book, or referencing its concepts."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Computational Global Macro: Game Theory, Machine Learning, and Causal Inference
**Author**: Joseph Simonian | **Pages**: ~186 | **Chapters**: 6 | **Generated**: 2026-11-21

## How to Use This Skill

- **Without arguments** — load core frameworks for reference
- **With a topic** — ask about `stag hunt`, `noisy-or`, `backdoor adjustment`, or another indexed topic; I find and read the relevant chapter
- **With chapter** — ask for `ch05`; I load that specific chapter
- **Browse** — ask "what chapters do you have?" to see the full index

When you ask about a topic not covered in Core Frameworks below, I will read
the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

The book's pipeline: scope the theme (Ch 1) → model the interaction as a game and simulate it (Ch 2-4) → make the causal structure explicit (Ch 5) → express the view in weights (Ch 6). The author calls this **computational global macro**: a quantitative footing for **thematic global macro**, written against geopolitical research that reads like "op-ed columns with charts."

### 1. Scope the theme (Ch 1)
- **Geopolitical risk** = "any potential detriment to a portfolio's positions stemming from political and political-economic actions within and among states and/or non-state actors."
- **Three levels of analysis** (adapted from Waltz): **individuals** (leaders), **states** (domestic institutions), **interstate relations**. Assess all three together.
- **Worldview first**: **Realism** (states seek security or power and value *relative* gains, so games look zero-sum) versus **Liberalism** (interdependence, institutions, *absolute* gains).
- **Internal versus external drivers**: is the policy change pushed from inside the state (lobbies, hawks and doves) or from outside (a rival's action)?
- Agents are **bounded**, **diachronic** and **commitment-driven**, not pure maximizers.
- Cooperation needs an ongoing relationship, identifiable parties and known history (Axelrod and Hamilton).
- Track reach (which markets a conflict moves) and **frozen** conflicts as well as hot ones.

### 2. Choose the game (Ch 2-4)
| Situation | Game |
|---|---|
| Dominant self-interested act beats the joint optimum | Prisoner's Dilemma |
| Attack against defense of a status quo | Run-Pass (Attack-Defense) |
| Agreed cooperation, disputed terms | Battle of the Sexes |
| Safe alone against better together | Stag Hunt |
| Outlasting under per-round cost | War of Attrition |
| Market reading a policymaker | Signaling game |
| Leader and follower | Stackelberg |
| Catch-up race | Pursuit-Evasion (Homicidal Chauffeur hybrid) |
| Ranked beliefs about the opponent | Game with lexicographic beliefs |

- Do not assume wealth-maximizing preferences for political actors. Non-economic preferences can dominate.
- Players may pursue **maximizing difference**: a lower own payoff to worsen the opponent's.
- Prisoner's Dilemma fixes are **external** (state coercion, changed payoffs, uncertain punishment) or **internal** (reciprocity, **tit-for-tat**, norms). External fixes are second-order public goods.

### 3. Simulate it (Ch 2-5)
- **Bayesian game via contexts**: represent each opponent **type** as its own payoff matrix with a probability.
- **CMAB with UCB** (Ch 2): strategies are arms. Select a = argmax [ Q_t(a) + c·sqrt(log t / N_a(t)) ]. Update Q_t(a) by the running average. Use when actions do not change the state.
- **Q-learning** (Ch 4): Q(s,a) = (1-α)·Q(s,a) + α·(R(s,a) + γ·max Q(s',a')). Use when actions change the next state and decisions are sequential.
- **SARSA** (Ch 5): on-policy, Q(s,a) ← Q(s,a) + α[R + γ·Q(s',a') - Q(s,a)].
- **Thompson Sampling** (Ch 5): sample each arm from Beta(α_k + X_k, β_k + N_k - X_k) and pull the highest.
- Rules of use the author draws from his runs:
  - Type probabilities drove outcomes more than payoff sizes. Spend effort there.
  - Match the number of rounds to the real length of the interaction. The winning action changes over time.
  - Always rerun with perturbed inputs (sensitivity analysis).
  - Read results as who is *more likely* to yield or gain, not when.
  - "Inducing cooperation is hard": a one-unit payoff increase did what very high cooperation probabilities barely did.
  - UCB did better under low model uncertainty. Thompson Sampling did better under high uncertainty.
  - With a hidden confounder and variable payoffs, Q-learning beat SARSA.

### 4. Test whether cooperation lasts (Ch 3)
- **Shapley value**: average marginal contribution over all orderings. Use it to judge whether a split is fair.
- **Myerson value**: allocation weighted by **bargaining power**. Compare with each party's **reservation value**. A shortfall signals instability.
- **Gale-Shapley alliance formation**: match **lesser powers** to capacity-limited **greater powers**. A matching is stable if it has no **blocking pair**.
- **Correlated equilibrium**: a **correlating device** (for example an IMF report) lets actors coordinate without communicating. **Focal points** do it with no signal.

### 5. Make causality explicit (Ch 5)
- Name the definition in use: regularity (Hume), counterfactual, **manipulation**, probabilistic (Suppes), or **Granger**.
- Draw the **DAG** and write the **SCM**. Find the confounders.
- **Backdoor adjustment**: P(C=1 | do(A=1)) = Σ_b P(C=1 | A=1, B=b)·P(B=b).
- **Noisy-OR**: P(E|C) = 1 - Π(1 - p_i) for independent causes. Combine promoting and inhibiting sets: P(E|C+,C-) = [P(E|C+) + 1 - P(¬E|C-)] / 2.
- **Decision under causal ignorance**: score each candidate graph by its summed **probabilistic distance** and **counterfactual distance** to the others (the **total distance score**). Act on the lowest.

### 6. Express the view (Ch 6)
- Prefer optimization to ad hoc sizing: consistent, less biased, risk-calibrated, explainable.
- **LP, directional view**: maximize return with caps (bearish) or floors (bullish) on weighted correlation to the affected markets.
- **LP, causal view**: minimize total causal distance across buys and sells assigned to each causal scheme.
- **Black-Litterman**: prior μ0 = γΣw0, views C'μ1 = M. **Ordinal Black-Litterman** takes rankings. **Robust Black-Litterman** adds a KL-bounded set of priors for covariance doubt.
- **GAN scenarios**: synthetic "alternative market histories" for robustness testing.
- **Epistemic Shapley value**: merge a team's linked probabilities coherently. Never average them directly.

### Caveat on the source
The book's examples are deliberately minimal and several printed tables and formulas contain inconsistencies. Each chapter file lists them under **Extraction Notes**. Check that section before reusing a number.

---

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-rationality-and-international-relations.md) | Theories of Human Rationality and International Relations | Geopolitical risk definition, three levels of analysis, worldview (Realism, Liberalism), internal vs external drivers, bounded rationality, Axelrod-Hamilton conditions |
| [ch02](chapters/ch02-conflict.md) | Conflict | Prisoner's Dilemma and its external and internal solutions, maximizing difference, Run-Pass game, Bayesian games, CMAB with UCB |
| [ch03](chapters/ch03-cooperation.md) | Cooperation | Coordination games, Stag Hunt, Shapley value, Gale-Shapley alliance formation, Myerson value, correlated equilibrium |
| [ch04](chapters/ch04-games-with-complex-interaction.md) | Games with Complex Interaction | Q-learning and MDPs, War of Attrition, signaling game, Stackelberg game, Pursuit-Evasion, lexicographic beliefs |
| [ch05](chapters/ch05-causal-inference.md) | Causal Inference in Models of Strategic Interaction | Definitions of cause, do operator, SCM, backdoor adjustment, SARSA, Noisy-OR, Colonel Blotto, Thompson Sampling, causal distance |
| [ch06](chapters/ch06-portfolio-construction.md) | Portfolio Construction | LP for directional and causal views, MVO, Black-Litterman, Ordinal BL, robust BL, GAN robust optimization, epistemic Shapley value |

## Topic Index

- **Absolute vs relative payoffs** → ch01, ch02
- **Alliance formation (Gale-Shapley)** → ch03
- **Backdoor adjustment** → ch05
- **Battle of the Sexes / Central Banks** → ch03, ch05
- **Bayesian games, types, contexts** → ch02
- **Black-Litterman, Ordinal BL, robust BL** → ch06
- **Bounded rationality, satisficing** → ch01
- **Causal distance (probabilistic, counterfactual)** → ch05, ch06
- **Causal reinforcement learning** → ch05
- **Central bank games** → ch03, ch04
- **CMAB, multi-armed bandits** → ch02, ch03
- **Colonel Blotto game** → ch05
- **Commitments, norms, social roles** → ch01, ch02
- **Correlated equilibrium, focal points** → ch03
- **Definitions of cause (Hume, Suppes, Granger)** → ch05
- **do operator, DAG, SCM** → ch05
- **Free-rider problem, public goods** → ch01
- **GAN robust optimization** → ch06
- **Geopolitical risk, levels of analysis** → ch01
- **Hoover's classification of economic causality** → ch05
- **Judgment aggregation, epistemic Shapley value** → ch06
- **Lexicographic beliefs** → ch04
- **Linear programming for views** → ch06
- **Maximizing difference** → ch02
- **Mean-variance optimization** → ch06
- **Myerson value, bargaining power, reservation value** → ch03
- **Noisy-OR model** → ch05
- **Prisoner's Dilemma, tit-for-tat** → ch02
- **Pursuit-Evasion, Homicidal Chauffeur** → ch04
- **Q-learning, MDP** → ch04
- **Realism, Liberalism, worldview** → ch01
- **Run-Pass, Attack-Defense** → ch02
- **SARSA** → ch05
- **Sensitivity analysis** → ch02, ch04
- **Shapley value** → ch03, ch06
- **Signaling game, signal quality** → ch04
- **Stackelberg game** → ch04
- **Stag Hunt** → ch03
- **Thompson Sampling** → ch05
- **Upper Confidence Bound (UCB)** → ch02, ch05
- **War of Attrition** → ch04

## Supporting Files

- [glossary.md](glossary.md) — all key terms with definitions
- [patterns.md](patterns.md) — all techniques and design patterns
- [cheatsheet.md](cheatsheet.md) — quick reference tables and decision guides
- Full text: `/home/ak/.local/share/book-to-skill/fulltext/simonian-computational-global-macro/full_text.txt` — grep it for depth the chapter files omit (local extraction, not shipped)

---

## Scope & Limits

This skill covers the book content only. For hands-on implementation in your codebase,
combine with project-specific tools. For topics beyond this book, check related skills
or ask the agent directly.

The extraction left 91 equations undecoded and 26 figures as image placeholders. The equations and payoff tables that define each chapter's main models were recovered from the original PDF and are marked with the PDF page. Most simulation charts were not read; where a chart was read, the chapter says so. The book contains no code. Its algorithms are given as tables and are reproduced as pseudocode.
