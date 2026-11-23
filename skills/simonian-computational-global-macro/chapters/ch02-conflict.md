# Chapter 2: Conflict

## Core Idea
Geopolitical conflict is modeled as a noncooperative game whose payoffs reflect heterogeneous, often non-economic preferences. Because real interactions are repeated and the opponent's type is uncertain, simulate them as iterated Bayesian games with a Contextual Multi-Armed Bandit (CMAB) driven by the Upper Confidence Bound (UCB) rule, and read the long-run average payoff of each action.

## Frameworks Introduced

- **Agent preferences in geopolitics** (2.2): do not assume uniform preferences. States hold preferences over economics and trade, security, human rights, environment and culture. Non-economic preferences "may very well dominate" economic ones even though the decision moves markets.
  - Agents are rational in the Chapter 1 sense: bounded (including cognitive biases), both synchronic and diachronic, and often driven by commitments rather than desires.

- **Game basics** (2.3): a game is an m × n matrix of payoff pairs.
  - **Pareto optimal**: no other outcome makes one player better off without making another worse off.
  - **Nash equilibrium**: each player's action is the best response to the others' actions.
  - Equilibrium is guaranteed for every two-player game that (1) ends after a finite number of moves, (2) is zero-sum, (3) has players who know their own and the other's moves and preferences.

- **Prisoner's Dilemma (PD)** (2.4): single-stage PDs have two marks. (1) Defection is the dominating strategy. (2) Mutual defection is the only outcome that is not Pareto optimal. The individually dominant option and the cooperative option conflict.
  - In any repeated PD there are infinitely many outcomes sustainable as long-run equilibria, from mutually cooperative to mutually noncooperative (Morrow 1994).
  - **Tit-for-tat** (Axelrod 1984): cooperate in round one, then copy the other player's previous move. Best individual strategy in Axelrod's computer tournament. Pareto optimal if both follow it.
  - **Axelrod's basis of cooperation**: (1) cooperation can develop among purely self-interested agents if small groups base it on reciprocity and will meet again. (2) A reciprocity strategy can thrive among diverse strategies. (3) Once established, it resists invasion by less cooperative strategies. Footnote: cooperation is an **Evolutionarily Stable Strategy (ESS)** under local interaction and imitation (Eshel et al. 2000; Maynard Smith 1982).
  - Precondition: "a sufficiently large chance for future interaction."

- **External versus internal solutions to the PD** (2.4.1):
  - **External**: change the rules of the game by incentive or coercion.
    - *Centralized*: concentrated in a few hands, such as the state (Hobbes).
    - *Change the payoff structure*: Ullmann-Margalit's mortar men with mines (Table 2.2).
    - *Threat of punishment*: mortar men with discipline (Table 2.3). The sanction's probability is uncertain.
    - *Persuasion* also counts as external.
    - Caveat (Ostrom 1990): external solutions are **second-order** collective action problems. Supplying the new rules is itself a public good.
  - **Internal** (spontaneous): no change in the game. Agents cooperate voluntarily. Consistent with reciprocity. Axelrod's trust-building is internal.
  - Two errors both kinds of solution correct: (1) that self-interest is the one privileged motive, (2) that each act of cooperation has a single motive. Cooperation occurs when motives reinforce each other (Elster 1990).

- **Norms as PD solutions** (2.4.2):
  - Exogenous norms: if observance changes the payoff structure, cooperation stabilizes.
  - Endogenous norms: "A spontaneous norm that solves a PD problem contains the same PD problem in itself." Promise-keeping builds trust and is exploitable for that reason.
  - Moral rules (Gauthier 1986): principles that raise cooperation in PD situations. Ullmann-Margalit's added condition: no "disadvantage to anyone extraneous to the PD-structured situation." The text finds no conclusive way to separate PD norms from moral norms.
  - Practical rule: work out which norms the actors are governed by before building the model.

- **Maximizing difference** (2.5): players often give up some absolute payoff to worsen the opponent's position (Marvell and Schmitt 1968). Treat the sacrificed payoff as a cost paid for relative position.

- **Attack-Defense Game / Run-Pass Game** (2.6): one player wants to change the status quo, the other to preserve it. Run-Pass is a variant of Matching Pennies.
  - Applications named in the text: political-military conflict, trade negotiation (which of two concessions to request), central-bank interaction (replace Run/Pass with Lower Rates/Maintain Rates).
  - Negotiations are not zero-sum, but payoffs can be read as "the amount of relative benefit transferred" between the parties (footnote 12).

- **Bayesian game via contexts** (2.7): a game of incomplete information. A **context** is the state of the world and represents a player's **type**, expressed as a distinct payoff matrix. Any game can be made Bayesian by pairing payoff matrices and attaching a probability to each context.

- **CMAB simulation of an iterated game** (2.8):
  1. At each step t, present a context. Each context has a probability of materializing.
  2. The agent chooses action a from K actions and receives reward r.
  3. Each payoff has a probability. The simulation computes **expected payoffs**: gain (loss) amount times its probability.
  4. Track the average payoff per action over time, from one player's point of view (Player 1 by convention). Repeat from each player's view for the full picture.
  5. Run a sensitivity analysis: change a key input, rerun, compare trajectories.
  - Payoff magnitudes "need not be precisely calibrated." Relative differences are enough.
  - Why CMAB: tractable and transparent. Limit (footnote 14): the agent's action does not change the state. Chapter 4's Q-learning removes that limit.

## Key Concepts
- **Dominating strategy**: best regardless of the opponent's play.
- **Defection / cooperation**: confessing / not confessing in the PD story.
- **Altruism**: serving the public good to benefit others, with empathy as its usual source. Distinguish from self-interested acts that only look altruistic because the agent's welfare is tied to the group.
- **Negative externalities**: unintended negative consequences (footnote 9).
- **Multi-armed bandit**: a slot machine with several arms, each an action. Goal: maximize cumulative payoff or minimize expected regret.
- **Arm**: one of a player's available strategies.
- **Exploitation vs exploration**: choosing the known best option versus trying an option of unknown benefit.
- **Type**: a player's character or nature in a Bayesian game.
- **Expected payoff**: gain or loss times the probability it obtains.

## Mental Models
- **Use the PD when an individually dominant act conflicts with the collective optimum**, for example free riding.
- **Use Run-Pass when one side attacks a status quo and the other must guess where.**
- **Think of each simulation iteration as a real unit of time** (month, year). Set the run length to the real length of the bout of interaction, because the winning action changes over time.
- **Think of an opponent's type as a context with a probability**, not as a known fact.
- **Ask whether payoffs are absolute or relative before reading the equilibrium.** Under relative-gain motives the standard equilibrium can mispredict (Table 2.4).

## Anti-patterns
- **Assuming wealth or profit maximization for political actors**: acceptable in economics, blocked in geopolitics.
- **Modeling a multi-period exchange as one shot**: most strategic exchanges run over extended time.
- **Trusting payoff sizes over type probabilities**: in the worked example the type probability, not the payoff size, drove the long-run result.
- **Reading only the long-run average**: Pass led early and Run led late in the same simulation.
- **Skipping sensitivity analysis.**
- **Assuming absolute payoffs** in a relative-gain setting.

## Reference Tables

Payoffs are (Player 1, Player 2), or (Offense, Defense). Tables 2.1 to 2.3 were legible in the extraction. Tables 2.4 to 2.8 were scrambled there and are recovered from the PDF as marked.

**Table 2.1. Prisoner's Dilemma** (PDF p. 45)

| | P2 Cooperate | P2 Defect |
|---|---|---|
| **P1 Cooperate** | 1, 1 | 0, 10 |
| **P1 Defect** | 10, 0 | 5, 5 |

**Table 2.2. Mortar Men with Mines** (PDF p. 49)

| | P2 Fight | P2 Desert |
|---|---|---|
| **P1 Fight** | 1, 1 | -2, -2 |
| **P1 Desert** | -2, -2 | -2, -2 |

**Table 2.3. Mortar Men with Discipline** (PDF p. 49)

| | P2 Fight | P2 Desert |
|---|---|---|
| **P1 Fight** | 1, 1 | -2, (-1, 0) |
| **P1 Desert** | (-1, 0), -2 | -1.5, -1.5 |

The deserter's payoff is -1 or 0 "depending upon whether a player is caught and executed or not." The -1.5 for joint desertion combines the undesirability of capture with the probability of execution.

**Table 2.4. Maximizing Difference** (recovered from PDF p. 54)

| | Column 1 | Column 2 |
|---|---|---|
| **Row 1** | 10, 10 | 3, 2 |
| **Row 2** | 9, 3 | 2, 1 |

Standard equilibrium: Row 1, Column 1. Most common experimental result: Row 2, Column 1.

**Table 2.5. Run-Pass Game 1** (recovered from PDF p. 55). Used as the Strong context.

| | Defend Pass | Defend Run |
|---|---|---|
| **Pass** | 0, 0 | 10, -10 |
| **Run** | 5, -5 | 0, 0 |

**Table 2.8. Run-Pass Game 2** (recovered from PDF p. 58). Used as the Weak context.

| | Defend Pass | Defend Run |
|---|---|---|
| **Pass** | -2, -1 | 3, -3 |
| **Run** | 2, -2 | -3, -2 |

**Tables 2.6 and 2.7. Opponent of unknown strength** (recovered from PDF p. 58). Player 2 is strong with probability α and weak with probability 1 - α.

| Strong opponent | P2 Fight | P2 Capitulate |
|---|---|---|
| **P1 Fight** | -1, 1 | 1, 0 |
| **P1 Capitulate** | 0, 1 | 0, 0 |

| Weak opponent | P2 Fight | P2 Capitulate |
|---|---|---|
| **P1 Fight** | 1, -1 | 1, 0 |
| **P1 Capitulate** | 0, 1 | 0, 0 |

**Table 2.9. Upper Confidence Bound Algorithm** (recovered from PDF p. 60)

```
For K possible actions, at any time t > K
Initialize, for all actions a:
    N_a(t) <- 0
    Q_t(a) <- 0
Repeat for t = 1, 2, ...:
    a      <- argmax_a ( Q_t(a) + c * sqrt( log t / N_a(t) ) )
    r      <- reward(a)
    N_a(t) <- N_a(t) + 1
    Q_t(a) <- Q_t(a) + (1 / N_a(t)) * ( r - Q_t(a) )
```

- Q_t(a): average real-valued payoff to action a. N_a(t): number of times a was taken.
- sqrt(log t / N_a(t)): "the confidence interval for the average reward."
- c: constant controlling the degree of exploration.
- The author picks UCB as "a balance between effectiveness and simplicity." Thompson Sampling is the alternative (Chapter 5).

## Worked Example

**Bayesian Run-Pass simulation** (2.8). Contexts: Table 2.5 (Strong) and Table 2.8 (Weak).

| Input | Value |
|---|---|
| P(Offense is Strong Passer) | 0.30 |
| P(Offense is Weak Passer) | 0.70 |
| P(Offense is Strong Runner) | 0.60 |
| P(Offense is Weak Runner) | 0.40 |
| P(success given Pass, Strong Passer) | 0.70 |
| P(success given Pass, Weak Passer) | 0.40 |
| P(success given Run, Strong Runner) | 0.80 |
| P(success given Run, Weak Runner) | 0.30 |
| Iterations | 10^5 games |

Arm design: six arms. Two arms draw the type for Run and the type for Pass and are always pulled. Four arms hold the success probabilities of the action combinations, and only the two matching the drawn types are pulled. So four of six arms are used per iteration.

Result, first run (Figure 2.1): Run has the higher average payoff over the full run. This holds although Pass has the larger positive payoffs in both contexts (10 and 3 against 5 and 2). The 0.70 weight on the Weak Passer type outweighs the payoff of 10 and the 0.70 success probability of the Strong Passer. Pass leads in the earliest iterations. The lead oscillates until just before 10^1 iterations, then Run takes over. Read from the figure on PDF p. 62: Run settles near 2.2, Pass near 0.9 (approximate chart reading, not stated in the text).

Sensitivity run (Figure 2.2): P(Strong Passer) raised from 0.30 to 0.40. The trajectories change markedly, but Run again has the higher long-run average. Read from the figure on PDF p. 63: Run near 2.2, Pass near 1.0 (approximate chart reading).

Author's conclusions: (1) the type probability assigned to Pass predominantly drives both runs, so probability accuracy matters more than payoff size. (2) The number of rounds matters because the winner changes over time. (3) Similar results under further parameter changes would support confidence in the model's robustness.

## Key Takeaways
1. Start from each actor's actual preferences. Non-economic preferences can dominate.
2. Pick the game form by structure: PD for dominance against the collective optimum, Run-Pass for attack against defense.
3. For a PD, list the available solutions: external (state coercion, changed payoffs, uncertain punishment, persuasion) and internal (reciprocity, norms).
4. Encode opponent uncertainty as types with probabilities. Simulate with CMAB and UCB.
5. Spend effort on type probabilities. They drove the outcome more than payoff magnitudes.
6. Match the simulation horizon to the real interaction length and inspect the whole path.
7. Rerun with perturbed inputs before trusting a ranking of actions.

## Connects To
- **Ch 1**: bounded, diachronic, commitment-driven rationality. Realism's relative gains become "maximizing difference."
- **Ch 3**: the same CMAB method applied to cooperative games.
- **Ch 4**: Q-learning, where actions change the state.
- **Ch 5**: Thompson Sampling as an alternative bandit algorithm.
- **External**: Osborne and Rubinstein (1994), Axelrod (1984), Ullmann-Margalit (1977), Ostrom (1990), Auer (2002), Chu et al. (2011).

## Extraction Notes
- In the extraction, sections 2.1 and 2.2 appear before the "Chapter 2" heading.
- Tables 2.4, 2.5, 2.6, 2.7 and 2.8 were scrambled and Table 2.9's four formulas were undecoded. All were recovered from the PDF as marked.
- Figures 2.1 and 2.2 are image placeholders in the extraction. The long-run levels quoted above are my reading of the PDF charts.
- Source inconsistency, Table 2.1: with larger numbers as better payoffs, defection dominates, but mutual defection (5, 5) is better for both players than mutual cooperation (1, 1). That contradicts the text's claim that mutual defection is Pareto inferior. Reading the numbers as jail terms does not fit the story either. The table is reproduced as printed.
- Source oddity, 2.4.1: the text says the -1.5 payoff is "less desirable than the payoff of getting caught," while the caught payoff is given as -1 or 0. Reproduced as printed.
- Source oddity, 2.8: "chance of success" is defined once, as the probability that Offense will Run while Defense defends Pass, and is then applied to both actions.
- Source oddity, 2.8: the text says the game is "relatively stable and sensitive to a rather moderate change in the input parameters." The surrounding argument suggests the intended sense is that the ranking survived the change. Not corrected.
- The text cites "Axelrod (1981)" in footnote 13 and "Axelrod (1984)" in 2.4.
