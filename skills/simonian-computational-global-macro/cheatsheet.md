# Cheatsheet: Computational Global Macro

## Which game?
| If the situation is... | Use | Ch |
|---|---|---|
| Dominant self-interested act beats the joint optimum (free riding, tariffs) | Prisoner's Dilemma | 2 |
| One side attacks a status quo, the other guesses where | Run-Pass (Attack-Defense) | 2 |
| Parties agree to act together, disagree on what to do | Battle of the Sexes | 3 |
| Safe solo option against better joint option needing trust (treaties, alliances) | Stag Hunt | 3 |
| Going alone yields nothing | Committed cooperators | 3 |
| Who blinks first under per-round cost | War of Attrition | 4 |
| How well the market reads the policymaker | Signaling game | 4 |
| One actor leads, others respond | Stackelberg | 4 |
| One actor is closing a gap on another | Pursuit-Evasion | 4 |

## Which learning rule?
- Actions do not change the state, short horizon: **CMAB**. Otherwise: **Q-learning**. (Ch 4)
- Low model uncertainty: **UCB**. High or changing uncertainty: **Thompson Sampling**. (Ch 5)
- Hidden confounder with variable payoffs: **Q-learning** beat **SARSA**. Observed state and fixed payoffs: no real difference. (Ch 5)

## Decision rules
- When payoffs may be relative, not absolute, expect "maximizing difference": players accept a lower payoff to hurt the opponent. (Ch 2)
- When a cooperation thesis rests on stated goodwill, discount it. Raising the payoff to cooperation moved the result. Raising the willingness barely did. (Ch 3)
- When an agreement was reached under pressure with weak measurable benefit, expect later violation. (Ch 3)
- When an allocation gives a party less than its reservation value, flag instability. (Ch 3)
- When explicit coordination is barred, look for a correlating device or a focal point. (Ch 3)
- When reading a simulation, rank who is more likely to yield. Do not read timing. (Ch 4)
- When the first-best action is played without exploration, check whether other cells pay more. (Ch 4)
- When estimating an effect with a common cause present, use the backdoor formula, not the raw conditional. (Ch 5)
- When several causal stories are plausible and none can be confirmed, act on the one with the lowest total distance to the others. (Ch 5)
- When a team's probabilities are linked, do not average them. Use the epistemic Shapley procedure. (Ch 6)
- When bearish on a market, cap correlation to it as well as weight. (Ch 6)

## Thresholds and defaults the author commits to
| Item | Value | Ch |
|---|---|---|
| Signal quality | 1 - n/10, n = inconsistent statement pairs | 4 |
| Discount factor γ, learning rate α | each between 0 and 1 | 4 |
| Combining d_P and d_C under ignorance | equal weights (plain sum) | 5 |
| Binary node with 5 parents | 2^5 = 32 distributions in a full table | 5 |
| Black-Litterman τ | typically small | 6 |
| GAN example | learning rate 0.001, 1000 epochs, 200 scenarios | 6 |
| Simulation horizon | match rounds to the real interaction length | 2 |

## Solutions to a Prisoner's Dilemma
| Type | Mechanism | Caveat |
|---|---|---|
| External, centralized | State coercion | Supplying it is itself a public good |
| External, payoff change | Remove the gain from defecting ("mines") | Needs someone to impose it |
| External, punishment | Uncertain sanction ("discipline") | Weak if detection is unlikely |
| Internal | Reciprocity, tit-for-tat, norms | Needs repeated play, identity, memory |

## Allocation and aggregation tools
| Question | Tool | Ch |
|---|---|---|
| Is the split fair? | Shapley value | 3 |
| Is it stable given leverage? | Myerson value plus reservation values | 3 |
| Who allies with whom? | Gale-Shapley matching | 3 |
| How do several causes combine? | Noisy-OR | 5 |
| How does a team's view combine? | Epistemic Shapley value | 6 |

## Portfolio method by type of view
| View | Method | Ch |
|---|---|---|
| Directional, bearish or bullish | LP with correlation cap or floor | 6 |
| Competing causal schemes | LP minimizing total causal distance | 6 |
| Numeric, against a benchmark | Black-Litterman | 6 |
| Ranked | Ordinal Black-Litterman | 6 |
| Covariance in doubt | Robust Black-Litterman | 6 |
| Extreme or unseen scenarios | GAN-generated histories | 6 |

## Tells
- Research that reads like "op-ed columns with charts" has no framework behind it. (Preface)
- A loud conflict is not a broad one. Ask which markets it reaches. (Ch 1)
- Each added cause in a Noisy-OR raises the probability, even when each cause is unlikely. Check the cause list for padding. (Ch 5)
- The winning action can change with the number of rounds. Inspect the path, not only the end. (Ch 2)
