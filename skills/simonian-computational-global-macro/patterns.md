# Patterns: Computational Global Macro

Techniques and algorithms from the book. Each entry names its chapter. Formulas are in the chapter files.

## Scope a geopolitical theme
**When to use**: before any modeling.
**How**: state the worldview (Realism or Liberalism). Tag the level (individual, state, interstate). Tag the driver (internal or external). Judge reach: which markets can it move. List frozen conflicts as well as hot ones. (Ch 1)
**Trade-offs**: qualitative. State-level risk is hard to quantify, and country scores are only a rough analogue of credit ratings.

## Pick the game form
**When to use**: to turn a situation into a payoff matrix.
**How**: Prisoner's Dilemma for a dominant act against the joint optimum. Run-Pass for attack against defense. Battle of the Sexes for agreed cooperation with disputed terms. Stag Hunt for safe-alone against better-together. War of Attrition for outlasting. Signaling for reading a policymaker. Stackelberg for leader and follower. Pursuit-Evasion for catch-up races. Lexicographic beliefs for a ranked view of the opponent. (Ch 2, 3, 4)
**Trade-offs**: payoffs need only reflect relative differences, but the form chosen fixes the conclusions available.

## Iterated Bayesian game with CMAB and UCB
**When to use**: repeated interaction, uncertain opponent type, actions that do not change the state.
**How**: build one payoff matrix per type. Assign type probabilities and success probabilities. Treat strategies as arms. Select with UCB. Track average payoff per action over a horizon matched to the real interaction. Rerun with perturbed inputs. (Ch 2, 3)
**Trade-offs**: transparent and cheap. Cannot model actions that change the state. Results were driven by type probabilities more than payoff sizes.

## Q-learning simulation
**When to use**: sequential decisions where actions change future states.
**How**: define states, actions and rewards. Initialize Q. Update with the Table 4.1 rule. Vary learning and exploration rates. Read relative outcomes, not timing. (Ch 4)
**Trade-offs**: handles state transitions and uncertainty. Costlier for large state or action spaces.

## Signal-quality scoring
**When to use**: to set the clarity parameter for a central bank.
**How**: review a major policy expression, count pairs of inconsistent statements n, set quality = 1 - n/10. (Ch 4)
**Trade-offs**: objective and simple. The text gives no rule for n above 10.

## Fair-division check with the Shapley value
**When to use**: to judge whether an agreement's split is fair enough to last.
**How**: define the worth of each coalition. Average each party's marginal contribution over all orderings. Compare with the actual split. (Ch 3)
**Trade-offs**: axiomatic fairness. Ignores bargaining power.

## Stability check with the Myerson value and reservation values
**When to use**: negotiations with unequal leverage.
**How**: weight coalition worth by each party's bargaining power. Compare each allocation with the party's reservation value. A shortfall flags instability. (Ch 3)
**Trade-offs**: more realistic and more concentrated outcomes. Needs bargaining-power inputs.

## Alliance matching with Gale-Shapley
**When to use**: to map likely alliance structure between greater and lesser powers, or large and small central banks.
**How**: derive each side's rankings from research and revealed behavior. Set capacities. Find a stable matching with no blocking pair. Monitor events against it. (Ch 3)
**Trade-offs**: gives an equilibrium structure. Only as good as the assumed preferences.

## Backdoor adjustment
**When to use**: estimating the effect of A on C when B causes both.
**How**: P(C | do(A)) = sum over b of P(C | A, B = b) × P(B = b). (Ch 5)
**Trade-offs**: needs the confounders identified and measured.

## Noisy-OR aggregation
**When to use**: several independent promoting and inhibiting causes of one effect.
**How**: assign each cause a probability. Compute 1 minus the product of (1 - p_i) for each set. Combine the two sets with eq. 5.16. (Ch 5)
**Trade-offs**: avoids exponential probability tables. Assumes independence and a complete cause list. Variants: leak, weighted, threshold, hierarchical, temporal.

## Bandit rule selection
**When to use**: choosing between UCB and Thompson Sampling.
**How**: UCB when model uncertainty is low. Thompson Sampling when reward distributions are uncertain or changing. (Ch 5)
**Trade-offs**: based on one simulated study with narrow and wide hidden-variable ranges.

## Causal-proximity selection
**When to use**: several plausible causal graphs and no way to pick the true one.
**How**: compute probabilistic and counterfactual distances between each pair. Sum each graph's distances to the others. Act on the lowest score. (Ch 5)
**Trade-offs**: partially effective across scenarios. Equal weighting of the two distances is the author's choice under ignorance.

## LP for directional and causal views
**When to use**: turning a bearish, bullish or causal view into weights or trades.
**How**: directional: maximize return with correlation caps or floors to the affected markets, a beta cap and bounds. Causal: minimize total causal distance with buys and sells per scheme summing to zero. (Ch 6)
**Trade-offs**: simple and transparent. Linear, so no risk term unless added as a constraint.

## Black-Litterman family
**When to use**: benchmark-relative portfolios with views.
**How**: BL for numeric views. OBL for ranked views. rBL when the covariance matrix is in doubt, with confidence p setting the KL neighborhood. (Ch 6)
**Trade-offs**: BL assumes normal returns. rBL is parametric.

## GAN scenario generation
**When to use**: testing robustness in scenarios beyond a parametric family.
**How**: train a Generator on return and covariance inputs. Produce many synthetic scenarios. Choose weights that maximize the Sharpe ratio across them. (Ch 6)
**Trade-offs**: non-parametric and wide-ranging. A complement to, not a replacement for, traditional robust methods.

## Epistemic Shapley aggregation
**When to use**: a team's linked probability estimates must be merged.
**How**: average to get ideal values. For each ordering of propositions, let earlier ones take ideal values and force later ones to coherence. Average across orderings. Iterate for precision. Weight managers by adjusting ideal values. (Ch 6)
**Trade-offs**: coherent and fair to each view. One pass is coherent only to about two decimals.
