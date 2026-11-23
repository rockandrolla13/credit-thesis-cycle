# Chapter 5: Causal Inference in Models of Strategic Interaction

## Core Idea
Correlation is not enough for geopolitical views. State which definition of cause is in use, write the causal structure as a DAG, estimate intervention effects with the do operator and backdoor adjustment, and combine multiple uncertain causes with the Noisy-OR model. When the true causal structure cannot be known, act on the candidate causal graph that is closest to all the others.

## Frameworks Introduced

- **Definitions of cause** (5.1; eqs. 5.1 to 5.13, recovered from PDF pp. 115-117):
  - (5.1) Hume, regularity: C causes E ≡ instantiations of E regularly follow instantiations of C. Based on "constant conjunction."
  - (5.2) Counterfactual: C causes E ≡ if C had not happened, E would not have happened either.
  - (5.3) Manipulation ("wiggle"): C causes E if manipulating C makes E change. "No causation without manipulation" (Holland 1986). The federal funds rate is the standard example.
  - (5.4 to 5.6) Suppes (1970) **positive cause**: t < t'. P(C_t) > 0. P(E_t' | C_t) > P(E_t').
  - (5.7 to 5.9) **Negative cause**: the same with P(E_t' | C_t) < P(E_t').
  - (5.10) Probabilistic manipulation: C causes E if manipulating C raises the probability that E will change.
  - (5.11, 5.12) **Granger (1969)**: x causes y if x temporally precedes y, and x provides more predictively useful information than a rival "naive" predictor. One formal expression: P(Y_t+1 | X_t, Y_t) > P(Y_t+1 | Y_t).
  - (5.13) General form: C causes E if there is information transmission from C to E.

- **Why economic causality is harder than natural-science causality** (5.1): (1) economies are open systems with many potential common causes and no access to experiments. (2) There are no "natural constants" (Hicks 1979). (3) Causes and effects are separated by significant lags.

- **Two uses of any causal model** (5.1): apply known causal knowledge, and discover unknown causal relations.

- **Hoover's classification of economic causality** (5.1; Table 5.1, Hoover 2008): structural (explanation) against process (prediction), crossed with a priori (theory identifies causes) against inferential (data identify causes). See Reference Tables.
  - **Financial data science (FDS)** is a hybrid, closest to the inferential process cell. For FDS, "accidental regularities" suffice if they forecast well and have enough history.

- **Causal inference process** (5.2): three steps.
  1. Identify the causal variables, using the research question, theory and domain knowledge.
  2. Establish the causal relationship while handling confounders, selection bias and counterfactual reasoning.
  3. Estimate the magnitude of the effect.
  - Techniques named: regression, **propensity score matching** (pair treated and control units by likelihood of treatment), **instrumental variables** (a variable correlated with the treatment that affects the outcome only through it), **difference-in-differences** (compare before-and-after changes across groups), and randomized controlled trials.
  - Effect types: **ATE** (average difference between treated and untreated groups), **CATE** (the same within a subgroup or condition), **ITE** (effect for one unit).

- **The do operator** (5.2.1; Pearl 2009): do(X = x) sets X externally, "independent of its observed causal relationships with other variables." It answers "what if" questions without changing the system.

- **Structural causal model (SCM)** (5.2.1): a DAG plus structural equations giving each variable as a function of its parents. Examples recovered from PDF pp. 122-123:
  - Common effect (Figure 5.1): HDI = β_GDP,HDI · GDP + β_PS,HDI · PS + β_FDI,HDI · FDI + ε. GDP, Political Stability and FDI each point to the Human Development Index.
  - Chain (Figure 5.2): B = β_AB · A + ε_B and C = β_BC · B + ε_C, with A = Expansionary Monetary Policy, B = Deposit Rates, C = Bank Loans.
  - Confounder (Figure 5.3): S&P 500 = β · Nikkei 225 + ε. KOSPI = β · S&P 500 + β · Nikkei 225 + ε. The Nikkei 225 points to both the S&P 500 and the KOSPI, and the S&P 500 points to the KOSPI.

- **Backdoor adjustment** (5.2.1): to estimate the effect of treatment A on outcome C, condition on the common causes of A and C. This is "closing the backdoor paths."
  - Formula (recovered from PDF p. 124): P(C = 1 | do(A = 1)) = Σ over b of P(C = 1 | A = 1, B = b) × P(B = b).

- **Causal reinforcement learning with an unobserved confounder** (5.3): a hidden state selects which game is being played.
  - Hidden "Global Trade Conditions": Free Trade gives a Battle of the Sexes, Mercantilist gives a Prisoner's Dilemma.
  - The hidden state's probabilities are drawn from a **Dirichlet distribution**. A larger concentration parameter alpha for a state makes it more likely.
  - Player 1 uses Q-learning. Player 2 uses **SARSA**.
  - Players update beliefs with a **Beta distribution**: alpha counts successes (rewards), beta counts failures (punishments). The players do not model the confounder explicitly.

- **SARSA (State-Action-Reward-State-Action)** (5.3): an **on-policy** algorithm. It updates with the action actually taken next under the current policy.
  - Update (eq. 5.14, recovered from PDF p. 127): Q(s, a) ← Q(s, a) + α [ R + γ × Q(s', a') - Q(s, a) ].
  - Contrast: Q-learning updates with the maximum Q-value of the next state.

- **Noisy-OR (NOR) model** (5.4): a probabilistic version of logical OR for a Bayesian (causal) network. It assumes causes act independently, so their joint effect can be computed without a full conditional probability table.
  - Problem solved: a binary node with five parents needs 2^5 = 32 distributions in its conditional probability table. Parameters grow exponentially with parents.
  - (5.15, recovered from PDF p. 132) P(E | C) = 1 - Π over C_i in C of (1 - p_i). Apply separately to promoting and inhibiting causes.
  - (5.16, recovered from PDF p. 132) P(E | C+, C-) = [ P(E | C+) + 1 - P(¬E | C-) ] / 2.
  - Property: adding a cause to the disjunction can raise the probability materially even when each cause is individually unlikely.
  - Inputs usually come from expert opinion.
  - **Leak probability** (Henrion 1987, footnote 16): a non-zero chance of the effect when no modeled cause is active.
  - Variants: **weighted NOR** (causes differ in strength), **threshold NOR** (a minimum number of active causes is needed), **hierarchical NOR** (higher-level causes activate lower-level ones), **temporal NOR** (influence varies over time, flagged as "of special interest to economists and investors").

- **Colonel Blotto game with NOR arms** (5.4): a two-player zero-sum game. Each player splits a fixed budget across battlefields without seeing the opponent's split. The larger allocation wins a battlefield, and a majority of battlefields wins the game.
  - Extension: two portfolio managers allocate capital to three countries. A NOR model over price stability, political stability and high labor productivity gives each country's probability of a strong economy. Those probabilities are the bandit arms.
  - A hidden confounder (an economic shock) scales each NOR probability up or down. It represents the uncertainty of the causal model for each country.

- **Thompson Sampling** (5.4; Table 5.3): for each arm k, hold a Beta(α_k, β_k) prior over its reward probability θ_k.
  1. At each step, sample a reward probability for every arm from its posterior and select the arm with the highest sample.
  2. Pull the arm.
  3. Observe success or failure and update.
  4. Repeat.
  - Posterior: Beta(α_k + X_k(t), β_k + N_k(t) - X_k(t)), where X_k(t) counts rewards and N_k(t) counts pulls.

- **Decision under causal ignorance: causal proximity** (5.5; Eva et al. 2019, adapted from Simonian 2022): when no single strategy works equally in all candidate causal scenarios, invest according to the scenario with the highest **causal proximity** to the others, so the strategy is "at least partially effective" if another scenario materializes.
  - **Probabilistic distance d_P(G, G*)**: count the conditional independencies entailed by one graph but not both, normalized by the number possible over the variable set. Based on the **Causal Markov Condition**.
  - **Counterfactual distance d_C(G, G*)**: count the counterfactual dependencies on which the graphs disagree, normalized by the number possible.
  - Combining them: Eva et al. offer a **lexicographic** approach (one measure narrows, the other breaks ties) and a **weighted** approach. The author uses the plain sum, the **total distance score**, which equals a 0.50 weight on each and assumes nothing about which measure is more correct.

## Key Concepts
- **Confounding variable**: influences both the dependent and independent variables and produces spurious effect estimates.
- **DAG**: directed acyclic graph, the visual form of a causal model.
- **Causal network / Bayesian network / belief network**: a DAG of conditional dependencies used for probabilistic inference.
- **Conditional probability table (CPT)**: the distributions of a node for every combination of parent states.
- **On-policy learning**: updating values using the policy actually followed.
- **Causal Markov Condition (CMC)**: conditional on all its direct causes, a node is independent of all variables that are not its direct causes or direct effects.
- **d-separation**: the graphical test of whether two nodes are independent given observed nodes.
- **Collider**: a node where both incoming edges on a path meet. The path is blocked unless the collider or a descendant is observed.
- **Non-collider / chain**: the path is blocked if the node (or a node in the chain) is observed.
- **Markov equivalence**: two DAGs with the same set of d-separations.

## Mental Models
- **Name your definition of cause before arguing about a cause.** Regularity, counterfactual, manipulation, probabilistic and Granger definitions license different claims.
- **Think of the policy rate as a manipulable common cause** of growth and inflation (footnote 2).
- **Use the Noisy-OR when several independent drivers push the same outcome** and a full probability table is impractical.
- **Use UCB when the causal model is fairly certain and Thompson Sampling when it is not.**
- **Under causal ignorance, prefer the decision that "works" across several causal scenarios** over one tailored to a single sequence of events.

## Anti-patterns
- **Treating association as causation**: associations "do not necessarily imply causation."
- **Ignoring the confounder**: a common cause of treatment and outcome biases the estimate unless the backdoor path is closed.
- **Building full CPTs for many-parent nodes**: computationally expensive.
- **Assuming all causes are in the model**: the basic NOR does. Add a leak probability.
- **Betting on one causal story** when the structure cannot be discerned.

## Reference Tables

**Table 5.1. Theories of Economic Causality** (source: Hoover 2008)

| | Structural | Process |
|---|---|---|
| **A Priori** | Cowles Commission; Koopmans (1953); Hood and Koopmans (1953) | Zellner (1979) |
| **Inferential** | Simon (1953); Hoover (1990, 2001); Favero and Hendry (1992); Angrist and Krueger (1999, 2001) | Granger (1969); Sims (1980) |

**Table 5.2. Noisy-OR probability tables** (effect: the stock price of a US oil company rises)

Single-cause probabilities, promoting: Fed funds cut 0.4, GDP up 0.2, unemployment down 0.3.
Single-cause probabilities, inhibiting: profit tax 0.3, OPEC quotas up 0.4, regulations up 0.1.

| Fed Funds ↓ | GDP ↑ | Unemployment ↓ | P(Stock ↑) | P(not Stock ↑) |
|---|---|---|---|---|
| F | F | F | 0 | 1 |
| F | F | T | 0.3 | 0.7 |
| F | T | F | 0.2 | 0.8 |
| F | T | T | 0.44 | 0.56 = 0.7 × 0.8 |
| T | F | F | 0.4 | 0.6 |
| T | F | T | 0.58 | 0.42 = 0.7 × 0.6 |
| T | T | F | 0.52 | 0.48 = 0.8 × 0.6 |
| T | T | T | 0.664 | 0.336 = 0.7 × 0.8 × 0.6 |

| Profit Tax ↑ | OPEC Quotas ↑ | Regulations ↑ | P(not Stock ↑) | P(Stock ↑) |
|---|---|---|---|---|
| F | F | F | 0 | 1 |
| F | F | T | 0.1 | 0.9 |
| F | T | F | 0.4 | 0.6 |
| F | T | T | 0.58 | 0.42 = 0.6 × 0.7 |
| T | F | F | 0.3 | 0.7 |
| T | F | T | 0.37 | 0.63 = 0.9 × 0.7 |
| T | T | F | 0.46 | 0.54 = 0.9 × 0.6 |
| T | T | T | 0.622 | 0.378 = 0.9 × 0.6 × 0.7 |

Panel B is reproduced as printed. See Extraction Notes on two rows.

**Modified games for the hidden-confounder simulation** (the source labels these Figures 5.6 and 5.7). Payoffs are drawn from the ranges.

| Battle of the Sexes | P2 Policy 1 | P2 Policy 2 |
|---|---|---|
| **P1 Policy 1** | [2,5], [1,4] | 0, 0 |
| **P1 Policy 2** | 0, 0 | [1,4], [2,5] |

| Prisoner's Dilemma | P2 Cooperate | P2 Defect |
|---|---|---|
| **P1 Cooperate** | [2,4], [2,4] | 0, [5,8] |
| **P1 Defect** | [5,8], 0 | [1,3], [1,3] |

**NOR bandit study inputs** (5.4). 100 units of capital, 10 rounds, 1,000 iterations.

| Input | Country 1 | Country 2 | Country 3 |
|---|---|---|---|
| Player 1 initial probability of a strong economy | 0.4 | 0.5 | 0.1 |
| Player 2 initial probability of a strong economy | 0.3 | 0.4 | 0.3 |
| P(strong economy given price stability) | 0.8 | 0.7 | 0.6 |
| P(strong economy given political stability) | 0.6 | 0.9 | 0.5 |
| P(strong economy given high labor productivity) | 0.7 | 0.5 | 0.8 |
| Hidden variable range, low uncertainty | (0.5, 0.6) | (0.2, 0.3) | (0.6, 0.8) |
| Hidden variable range, high uncertainty | (0.5, 1.1) | (0.2, 0.8) | (0.7, 1.3) |

**Table 5.4. Orientation Discovery Algorithm** (formulas recovered from PDF p. 142)

```
For each node X_i in V, build parent set pa(X_i) and child set ch(X_i).
OD(G1, G2)  = sum over X_i in V of [ δ(pa(G1, X_i), pa(G2, X_i)) + δ(ch(G1, X_i), ch(G2, X_i)) ]
δ(A, B)     = 1 if A != B, 0 if A = B
NOD(G1, G2) = OD(G1, G2) / |N|        (|N| = number of nodes)
```
The text states NOD lies between 0 and 1, and NOD = 0 implies the graphs are Markov equivalent.

**Table 5.5. Counterfactual Distance Algorithm** (formula recovered from PDF p. 143)

```
ref   = all possible counterfactual dependencies over V
list1, list2 = the dependencies each graph asserts
unshared = items of ref present in exactly one of list1, list2
NCD = (unshared elements count) / (ref count)
```

**Table 5.6. Distances between the three causal graphs**

| Pair | d_P | d_C |
|---|---|---|
| G1, G2 | 1/4 | 1/4 |
| G1, G3 | 0 | 1/6 |
| G2, G3 | 1/4 | 1/12 |

## Worked Example

**1. Backdoor adjustment** (5.2.1; numbers recovered from PDF p. 125). A = increased consumer spending, C = increased inflation, B = reduction in interest rates, which causes both.
- Given: P(C=1 | A=1, B=0) = 0.2. P(C=1 | A=1, B=1) = 0.8. P(B=0) = 0.6. P(B=1) = 0.4.
- P(C=1 | do(A=1)) = 0.2 × 0.6 + 0.8 × 0.4 = 0.44.
- Reading: a 44% probability of increased inflation when consumer spending is increased, net of the interest-rate effect.

**2. Noisy-OR for an oil stock** (5.4; eq. 5.17 recovered from PDF p. 132). With all three promoting and all three inhibiting causes true:
- P(E | C+) = 1 - (0.6 × 0.8 × 0.7) = 0.664.
- P(¬E | C-) = 1 - (0.7 × 0.6 × 0.9) = 0.622.
- P(E | C+, C-) = (0.664 + 1 - 0.622) / 2 = 0.521.
- Note in the text: each all-true panel result is above 0.50 although every single cause is below 0.50.

**3. Choosing a causal scheme under ignorance** (5.5.1). A portfolio team weighs three explanations of a fall in interest rates A, with B = consumer prices, C = stock market, D = real estate.
- G1: A → B, A → C, D unaffected.
- G2: A → D, B and C unaffected.
- G3: A → C, A → D, B unaffected.
- Total distance score = the sum of a graph's d_P and d_C to each other graph (Table 5.6).
  - G3: 0 + 1/6 + 1/4 + 1/12 = 0.50.
  - G1: 1/4 + 1/4 + 0 + 1/6 = 0.66.
  - G2: 1/4 + 1/4 + 1/4 + 1/12 = 0.83.
- Decision: if forced to pick one scheme, pick G3, the lowest score.

**4. Simulation findings stated in the text**
- Trade game, observed state, fixed payoffs, 20 rounds and 10,000 iterations (Figure 5.5): Q-learning and SARSA earn almost identical average payoffs, SARSA marginally ahead.
- Trade game, hidden state, ranged payoffs (Figure 5.8): payoffs for both are significantly lower. Q-learning performs significantly better than SARSA. The author's suggested reasons: updating on the maximum next Q-value is less sensitive to reward variance, and exploration adapts to hidden dependencies.
- NOR Blotto, narrow hidden-variable ranges (Figure 5.10): UCB performs significantly better than Thompson Sampling.
- NOR Blotto, wide ranges (Figure 5.11): Thompson Sampling "seems to be better suited." Suggested reasons: Bayesian modeling of uncertainty and a better exploration-exploitation balance.

## Key Takeaways
1. Write each thesis's causal claim in one of the chapter's explicit forms, so it can be tested.
2. Draw the DAG and identify common causes before estimating any effect.
3. Compute intervention probabilities with the backdoor formula, not raw conditionals.
4. Aggregate promoting and inhibiting drivers with equations 5.15 and 5.16.
5. Expect lower payoffs when the confounder is hidden and payoffs vary. In that setting Q-learning outperformed SARSA.
6. Match the bandit rule to model uncertainty: UCB for low, Thompson Sampling for high.
7. When the structure is unknowable, score candidate graphs by summed d_P and d_C and act on the most central one.

## Connects To
- **Ch 2**: UCB and bandit arms. Battle of the Sexes and Prisoner's Dilemma reused as the two hidden games.
- **Ch 4**: Q-learning, compared with SARSA here.
- **Ch 6**: section 6.2.1 expresses causal views such as P(C=1 | do(A=1)) in portfolios.
- **External**: Pearl (2009), Suppes (1970), Granger (1969), Hoover (2008), Eva et al. (2019), Simonian (2021, 2022).

## Extraction Notes
- Recovered from the PDF: eqs. 5.1 to 5.13 (pp. 115-117), SCM equations and DAG shapes for Figures 5.1 to 5.4 (pp. 122-124), the backdoor formula and its numbers (pp. 124-125), eq. 5.14 (p. 127), eqs. 5.15 to 5.17 (p. 132), the three scenario graphs (p. 140), and the OD, NOD and NCD formulas (pp. 142-143).
- Figures 5.5, 5.8, 5.9, 5.10 and 5.11 are image placeholders and were not opened. Results for them come from the text only.
- The extraction scrambles the order of the NOR bandit input list. The table above regroups it.
- Table 5.2 Panel A: the first cell of the last row is garbled in the extraction and reads True in context.
- Source inconsistency, Table 5.2 Panel B: with single-cause probabilities 0.3, 0.4, 0.1, the row (F, T, T) should give 0.46 and the row (T, T, F) should give 0.58. The printed values and products for these two rows appear swapped. The all-true row (0.622) and eq. 5.17 are consistent.
- Source oddity, 5.1: one sentence reads "In contrast to structural approaches, inferential approaches ... are primarily concerned with uncovering economic processes." The context suggests it means process approaches.
- Table 5.3 as printed says "θ_k where k ranges from 0 to 1."
- Table 5.4 step (2) as printed defines pa(X_i) as the nodes X_j such that X_i is d-separated from X_j given pa(X_j), and ch(X_i) analogously. Reproduced without interpretation. The text does not show the conditional independencies or counterfactual lists behind Table 5.6, so those distances cannot be re-derived from the chapter.
- The text rounds 2/3 to 0.66 and 5/6 to 0.83.
- The description of blocking conditions defines a non-collider as "a node where only one incoming edge exists."
