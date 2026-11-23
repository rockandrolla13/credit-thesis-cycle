# Chapter 4: Games with Complex Interaction

## Core Idea
When agents act in sequence and their actions change the state they face next, replace the bandit with Q-learning on a Markov Decision Process. The chapter applies it to five game forms, each tied to a central-bank, trade or resource-dispute case, and reads the result as "which player is more likely to" yield, lead, catch up or gain, not as a point forecast.

## Frameworks Introduced

- **CMAB versus Q-learning** (4.1): a selection rule.
  - Use a CMAB for shorter-term decisions under uncertainty where the agent affects only its reward in a given state.
  - Use Q-learning when (a) decisions are sequential and long-term consequences matter, (b) the best action depends on the history of actions and states, (c) the agent can influence the next state, (d) state transitions are uncertain or partly observable.
  - Example of (c): the Fed can influence the future macroeconomic states that it and other central banks face.
  - Cost: Q-learning keeps a value for every state-action pair, so it is more computationally demanding for large state or action spaces.

- **Markov Decision Process (MDP)** (4.2): a set of states, a set of actions (possibly state-dependent), a transition probability distribution for each state-action pair, and a reward or cost for each pair. Goal: find a **policy**, a mapping from states to actions, that maximizes expected long-term reward.

- **Q-learning** (4.2): estimates the **Q-function** Q(s, a), the expected cumulative reward from taking action a in state s and following the optimal policy afterwards. It follows the Bellman equation (1957).
  - Steps: (1) initialize Q-values for all state-action pairs. (2) Select an action with a rule balancing exploration and exploitation. (3) Receive a reward and observe the next state. (4) Update Q from the reward and the maximum Q-value of the next state. (5) Repeat until Q-values converge. (6) Read the optimal policy from the learned Q-values.
  - The author's implementation uses the UCB rule from Chapter 2 and, unless noted, randomly varies the learning rate α and the exploration rate in each iteration.

- **War of Attrition (WA)** (4.3): a sequential model of direct conflict. Each player decides when to retreat. Staying costs C and wins an object of value V. Played over a finite number of rounds, with players converging toward a Nash equilibrium.
  - Central-bank reading: V_i is the growth won by keeping policy easy. C_i is the inflationary pressure, observed or expected, incurred each round. A winner emerges when all banks but one stop easing.
  - Historical claim in the text: in the post-GFC easing war of attrition "the clear winner was Japan", which kept easing while the US, EU and UK began extended rate hikes.
  - Purpose: the simulation shows which player is more likely to give up, "not ... precisely when."

- **Signaling game** (4.4; Spence 1973): a **sender** with private information about its type transmits a costly signal to a **receiver**. A signal is credible when it is cheaper for the high type to send.
  - Monetary version: sender = central bank fighting inflation, receiver = the market. Types θ: Slightly Hawkish, Hawkish, Very Hawkish. Signals s: policy pronouncements or general commentary.
  - Signaling cost of a type = the inflation rate likely to materialize under that type's policy action.
  - Receiver payoff = expected equity return from correctly identifying the type. Misreading incurs a penalty (a negative return). Net payoff = raw payoff minus penalty.
  - **Signal quality parameter**, in the range 0 to 1: the clarity with which the bank conveys policy. Lower quality lowers the chance the receiver decides correctly.
  - **Objective estimate of signal quality**: review a major policy expression such as FOMC statements, count the pairs of inconsistent statements n, and set quality = 1 - n/10 (formula recovered from PDF p. 100).

- **Stackelberg game** (4.5): a sequential game with a **leader** who moves first and commits, and a **follower** who responds. Use it where one player has more power or influence, such as a major central bank leading smaller ones.
  - **Stackelberg equilibrium**: a strategy pair in which the leader's strategy maximizes its payoff given the follower's best response.
  - Beliefs matter: each bank holds beliefs about the other's **reaction function** and about economic conditions.
  - Leader's problem (eq. 4.1, recovered from PDF p. 102): max over a_f of Π_Fed(a_f, a_e*(a_f)), where a_e* is the ECB's response to the Fed's action.
  - Payoffs (eq. 4.2, recovered from PDF p. 102):
    - Π_Fed = -α1_Fed (action_af - π_target_Fed)^2 - α2_Fed (action_af - y_target_Fed)^2 - δ1_Fed (action_af - π_target_ECB)
    - Π_ECB = -β1_ECB (action_ae - π_target_ECB)^2 - δ1_ECB (action_ae - π_target_Fed)
  - α1, β1: weight each bank puts on its inflation target. α2: the Fed's weight on its employment target. Weights are relative and unrestricted in range.
  - δ: the **coordination penalty** for deviating from the other bank. A positive δ expresses a desire to align.
  - Actions are drawn randomly at the start of each round, for simplicity.
  - Use: vary the inputs to get a range of possible inflation outcomes per central bank, conditional on the assumed propensity to coordinate.

- **Pursuit-Evasion game** (4.6): a Pursuer P tries to make contact, an Evader E tries to avoid it.
  - Dynamics (eqs. 4.3, 4.4, recovered from PDF p. 105): dP(t)/dt = V_p(t) and dE(t)/dt = V_e(t).
  - **Proportional navigation** (eq. 4.5, recovered from PDF p. 105): V(t) = K * LOS_rate(t) * LOS_unit(t). LOS_rate is the derivative of the line of sight, LOS_unit its unit vector, K a scalar constant.
  - **Homicidal Chauffeur**: a variant in which the Chauffeur drives straight or swerves and the Victim stays or jumps. It differs from the standard game in three ways. The game ends when the Victim reaches a destination. The Chauffeur follows a predefined path. The Chauffeur aims to inflict harm.
  - **Hybrid trade-war game**: the author combines the Chauffeur's notion of harm with full pursuit dynamics. The Pursuer country tries to catch the Evader's export volumes. **Speed** is read as the effectiveness of a policy action.

- **Game with lexicographic beliefs** (4.7; Perea 2012): a player believes the opponent will act according to an order of preference or priority, and attaches probabilities to the ranked actions. Compute the expected payoff of each own action under those beliefs, then let the beliefs evolve under Q-learning.

## Key Concepts
- **Discount factor γ**: weight of future against immediate rewards, between 0 and 1.
- **Learning rate α**: weight of new information against the existing Q-value, between 0 and 1.
- **Exploration rate**: how often the agent tries non-greedy actions.
- **Sender / receiver**: the informed and uninformed players in a signaling game.
- **Reaction function**: how one bank adjusts its rate to the other's decision.
- **LOS rate**: derivative of the angle between the Pursuer's velocity vector and the vector joining Pursuer and Evader.
- **Informative prior** (footnote 4): a non-uniform prior over states.

## Mental Models
- **Use the War of Attrition for "who blinks first" problems** with a per-round cost and a prize for outlasting.
- **Use the signaling game when the question is how well the market can read the policymaker.**
- **Use Stackelberg when one actor sets terms and others respond.**
- **Use Pursuit-Evasion when one actor is closing a gap on another** and policies differ in effectiveness.
- **Think of exploration as insurance against a wrong prior.** In 4.7 the action with the highest initial expected payoff was not the best to play repeatedly.
- **Treat each round as a unit of time**, such as a month.

## Anti-patterns
- **Using a bandit where actions change the state**: the "most fundamental shortcoming" of CMABs.
- **Reading a simulation as a timing forecast**: it ranks who is likelier to give up.
- **Over-exploiting the first-best action**: Country B's near-continuous play of Action 1 left it worse off than Country A.
- **Positing signal quality subjectively when it can be counted** from inconsistent statements.

## Reference Tables

**Table 4.1. Q-learning** (recovered from PDF p. 93)

```
Bellman target:   Q(s, a) = R(s, a) + γ * max( Q(s', a') )
Update rule:      Q(s, a) = (1 - α) * Q(s, a) + α * ( R(s, a) + γ * max Q(s', a') )
```
R(s, a): immediate reward. s': next state. a': next action. γ and α are each between 0 and 1.

**Table 4.2. War of Attrition** (recovered from PDF p. 94, as printed)

| | P2 Continue Fighting | P2 Give Up |
|---|---|---|
| **P1 Continue Fighting** | V1 - C1, V2 - C2 | V1 - C1, -C2 |
| **P1 Give Up** | -C2, V2 - C2 | -C1, -C2 |

**Table 4.3. War of Attrition Game II** (recovered from PDF p. 95). Entries are value range minus cost range, redrawn each round.

| | ECB Maintain Easy Policy | ECB Halt Easing |
|---|---|---|
| **Fed Maintain Easy Policy** | [2, 6] - [2, 5], [1, 4] - [2, 4] | [2, 6] - [2, 5], 0 |
| **Fed Halt Easing** | 0, [1, 4] - [2, 4] | 0, 0 |

**Signaling game inputs** (4.4)

| Type | Signaling cost (inflation) | Payoff if identified (equity return) | Penalty if misread |
|---|---|---|---|
| Slightly Hawkish | 5% | 2% | 6% |
| Hawkish | 6% | 7% | 5% |
| Very Hawkish | 7% | 12% | 10% |

Runs: 20 rounds, 1,000 iterations, three signals. Signal quality 0.8 in the first run and 0.2 in the second.

**Stackelberg inputs** (Figure 4.4, recovered from PDF p. 103)

| Bank | Inflation target | Employment target | Inflation weight | Employment weight | Coordination penalty δ |
|---|---|---|---|---|---|
| Fed | 2.5% | 4% | α1 = 1.0 | α2 = 1.0 | 1.5 |
| ECB | 1.5% | none | β1 = 1.0 | none | 0.5 |

Run: 100 rounds, 1,000 iterations.

**Trade-war action speeds** (4.6)

| Action | Pursuer | Evader | Pursuer, second run |
|---|---|---|---|
| Reduce tariffs | 1.6 | 1.5 | 1.8 |
| Weaken currency | 1.8 | 1.7 | 1.8 |
| Export subsidies | 1.4 | 1.6 | 1.4 |
| Export tax rebates | 1.2 | 1.3 | 1.2 |

Other settings: ten states (levels of market access), a uniform 10% prior per state, a reward of 100 for capture and 10 - d otherwise, where d is the distance between the countries. Speeds carry random noise.

**Table 4.4. Game with Lexicographic Beliefs** (Country A, Country B)

| | B Action 1 | B Action 2 | B Action 3 |
|---|---|---|---|
| **A Action 1** | 3, 2 | 1, 3 | 4, 5 |
| **A Action 2** | 2, 4 | 2, 3 | 3, 1 |
| **A Action 3** | 1, 3 | 4, 1 | 2, 2 |

Action 1 = negotiate for shared use. Action 2 = unilateral exploitation. Action 3 = military action to occupy the territory.

## Worked Example

**Lexicographic beliefs, single round then simulation** (4.7; arithmetic recovered from PDF p. 110).

Country A believes B plays Actions 1, 2, 3 with probabilities 0.6, 0.3, 0.1. A's expected payoffs:
- Action 1 = (0.6 × 3) + (0.3 × 1) + (0.1 × 4) = 2.5
- Action 2 = (0.6 × 2) + (0.3 × 2) + (0.1 × 3) = 2.1
- Action 3 = (0.6 × 1) + (0.3 × 4) + (0.1 × 2) = 2.0

Country B believes A plays Actions 1, 2, 3 with probabilities 0.3, 0.2, 0.5. B's expected payoffs:
- Action 1 = (0.3 × 2) + (0.2 × 4) + (0.5 × 3) = 2.9
- Action 2 = (0.3 × 3) + (0.2 × 3) + (0.5 × 1) = 2.0
- Action 3 = (0.3 × 5) + (0.2 × 1) + (0.5 × 2) = 2.7

Both prefer Action 1, so negotiation is preferred after one round.

Simulation: 50 rounds, 1,000 simulations, exploration and learning rates 0.1 for both.
- Result (Figure 4.7): Country A ends up better off. B's near-continuous exploitation of Action 1 earns it 2 per round against A's 3 in the (Action 1, Action 1) cell.
- Rerun with B's exploration rate raised to 0.7 (Figure 4.8): exploration favors B, because most cells other than (Action 1, Action 1) pay B relatively more.
- Lesson in the text: exploration helps an agent find beneficial actions that differ from its initial view of the best one.

**Other simulation results stated in the text**
- War of Attrition, Fed against ECB, 24 rounds and 1,000 iterations (Figure 4.1): the Fed is "in a somewhat better position to withstand the risk of higher inflation" given the inputs.
- Signaling, quality 0.8 (Figure 4.2): net payoff fluctuates in a tight range and the market learns over the rounds. Quality 0.2 (Figure 4.3): still range-bound but less tightly, at a markedly lower level, with little visible learning.
- Stackelberg (Figure 4.4): the Fed, with the larger δ, makes more effort to coordinate and its optimal inflation target trends lower toward the ECB's. The ECB's target rises toward its stated 1.5%.
- Trade war (Figure 4.5): closely contested until round seven, then the Evader breaks away. With the Pursuer's "reduce tariffs" speed raised to 1.8 (Figure 4.6), the Pursuer eventually overtakes, but only after several rounds of learning.

## Key Takeaways
1. Choose Q-learning over a CMAB whenever the actor's move changes the next state.
2. Read attrition results as relative staying power. Net payoff per round is value minus cost.
3. Policy clarity is measurable. Lower signal quality cut the market's net payoff and its learning.
4. In a leader-follower setting, the size of the coordination penalty decides who moves toward whom.
5. Small changes in one policy's effectiveness can reverse a catch-up race, after a learning lag.
6. Seed beliefs as probabilities over the opponent's ranked actions, compute expected payoffs, then stress them with different exploration rates.
7. Every example is a deliberately simple setup. The author invites refinement of inputs and payoffs.

## Connects To
- **Ch 2 and Ch 3**: CMAB and UCB, Bayesian games, exploration against exploitation.
- **Ch 5**: SARSA and Thompson Sampling extend the reinforcement learning toolkit, with causal structure added.
- **Ch 6**: the views these simulations produce are expressed in portfolios.
- **External**: Watkins and Dayan (1992), Bellman (1957), Spence (1973), Stackelberg (1934), Isaacs (1965), Perea (2012).

## Extraction Notes
- Recovered from the PDF: Table 4.1 (p. 93), Tables 4.2 and 4.3 (pp. 94-95), eqs. 4.1 and 4.2 (p. 102), Figure 4.4 inputs (p. 103), eqs. 4.3 to 4.5 (p. 105), the expected-payoff arithmetic (p. 110), the signal quality formula and the "10 - d" reward (the extraction printed "1 -n 10" and "10 d").
- Figures 4.1, 4.2, 4.3, 4.5, 4.6, 4.7 and 4.8 are image placeholders and were not opened. Only the text's verbal description of them is used.
- Source inconsistency, Table 4.2: the lower-left cell prints Player 1's payoff as -C2, while the text says Player 1 "incurs cost C1." Reproduced as printed.
- Source inconsistency, Table 4.3: its "halt easing" payoffs are 0, while Table 4.2 gives -C to a player who gives up. The row label is printed "Halt Easting."
- Source oddity, 4.5: the text says the leader has "the ability to observe the follower's actions before making a decision", which reverses the usual order and the text's own later description.
- Source oddity, eq. 4.2: the coordination terms are printed unsquared, and the employment term compares the action with the employment target directly. Reproduced as printed.
- Source oddity, 4.5: the text says the ECB "eventually achieves its stated target of 1.5%". The ECB chart on PDF p. 103 ends just below 1.5.
- Table 4.1 as printed says a' is "the next action the agent selects in state s", not s'.
