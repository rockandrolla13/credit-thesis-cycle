# Chapter 3: Cooperation

## Core Idea
Cooperation is a coordination problem with several equilibria, and the Stag Hunt is its template: a certain small payoff competes with an uncertain large one. Simulation shows inducing cooperation is hard. Once cooperation exists, test whether it will last with three tools: the Shapley value (is the split fair?), the Gale-Shapley algorithm and Myerson value (is the structure stable?), and correlated equilibrium (is there a signal to coordinate on?).

## Frameworks Introduced

- **Coordination games** (3.1): coordination problems arise when a game has multiple equilibria and decisions are interdependent.
  - **Pure coordination (Driving Game)**: two pure Nash equilibria, both Pareto efficient. Which one is chosen does not matter.
  - **Battle of the Sexes**: both players want to act together but prefer different joint actions. Two Nash equilibria with unequal payoffs.
  - **Battle of the Central Banks**: the same structure with the Fed preferring a joint hike and the ECB preferring a joint hold (Table 3.3).

- **Stag Hunt (SH)** (3.2; Skyrms 1996, 2004): each hunter chooses Stag or Hare without knowing the other's choice. Stag needs both. Hare can be caught alone.
  - Two pure-strategy Nash equilibria: both cooperate, or both defect. The PD has only one (both defect).
  - **Assurance problem**: the cooperator who is abandoned is the "sucker" and takes a negative payoff. The risk is one of trust.
  - Geopolitical instances in the text: Brexit (the UK chose to "hunt a hare"), compliance with the Nuclear Non-Proliferation Treaty (collective security is the stag, own weapons the hare), NATO commitments (Turkey's separate security relations with Russia as a hare).

- **Evolutionarily committed cooperators** (3.2): a second reading of cooperation. Cooperation does not raise the resources each member gets. It raises the probability of getting any. Mutual cooperation is the only cell with a positive payoff (Table 3.5). Here there is no assurance problem because going alone is "evolutionary suicide."
  - Evidence from primate field studies: groups form (1) when predation is frequent, for surveillance, and (2) when same-species competition for food is dense. Where both are low, a solitary life develops (orangutans).
  - Rule for choosing the game: ask which actions the players would consider rational. In nature the environment decides. For humans the social and institutional context decides (Sunstein's social role, Chapter 1).

- **CMAB simulation of a cooperative game** (3.3): the Chapter 2 method, with contexts for a High Value and Low Value Stag, a probability of each context, a probability of cooperation given the context, and a constant Hare payoff as the reference.

- **Shapley value (SV)** (3.4; Shapley 1953): a fair-division solution for a **transferable utility game (TUG)** (N, υ), where N = {1, ..., n}, υ maps every subset of N to a real number and υ(∅) = 0. υ(S) is the **worth** of coalition S.
  - How: take every ordering ω of the players. For each ordering, compute each player's marginal contribution to its predecessors P_ω^i. Average over all n! orderings.
  - Equations (recovered from PDF p. 80):
    - (3.1) m_i^ω(N, υ) := υ(P_ω^i ∪ i) - υ(P_ω^i)
    - (3.2) φ_i(N, υ) = (1/n!) Σ over ω in Ω(N) of m_i^ω(N, υ), for i in N
  - Axioms as printed (recovered from PDF p. 80):
    - (3.3) Efficiency: Σ over i in N of φ_i(υ) = υ(N)
    - (3.4) Symmetry: υ(S ∪ {i}) = υ(S ∪ {j}), for every S of N
    - (3.5) Additivity: φ_i(υ + w) = φ_i(υ) + φ_i(w)
    - (3.6) Null Player: i is null in υ if υ(S ∪ Z{i}) = υ(S) for all S
  - Investor use: perceived fairness of the final allocation is "an important determinant" of whether an agreement holds. If an agreement looks unlikely to hold, the investor "may refrain from investing in countries and regions affected."

- **Gale-Shapley alliance formation (Algorithm 3.1)** (3.5; Gale and Shapley 1962): the hospital-resident problem with **greater powers** G as hospitals and **lesser powers** L as residents. Each greater power g has capacity c_g.
  1. Each lesser power l ranks a non-empty subset of G: p(l).
  2. Each greater power g ranks all lesser powers that ranked it: p(g).
  - A matching M is **valid** if every matched l is matched to a g in p(l), every g holds only lesser powers in p(g), and no g exceeds c_g.
  - A valid matching is **stable** if it has no **blocking pair** (l, g), meaning all three hold: mutual preference (each ranks the other), l is unmatched or prefers g to its current match, and g has spare capacity or prefers l to at least one of its current partners.
  - Where preferences come from: research on each country's economic strengths and challenges, and revealed behavior such as legislation that harmonizes an economy with a prospective partner.
  - How to use: compute the equilibrium alliance structure, then watch events to judge whether they "bode well or ill" for each alliance's stability over the investment horizon.
  - Also suggested: match large-economy central banks with small-economy central banks to test whether observed policy coordination is stable.

- **Myerson value (MV)** (3.5; Myerson 1977): like the SV but weighted toward stability. It allocates so that "no subset of players has the incentive to form a new coalition and deviate."
  - Equation (3.7) as printed (recovered from PDF p. 84): φ_i(υ) = Σ w(S) · δ_i(S), summed over all coalitions S ⊆ N that include i. w(S) is the worth of S, defined as υ(S). δ_i(S) is the **bargaining power** of i in S.
  - Bargaining power is "a function of its economic size, market access, and political and military influence."
  - **Reservation value**: the minimum offer a player accepts. If a player is allocated less than this, "it could be an indication that the solution is unstable."

- **Correlated equilibrium** (3.6; Aumann 1974): a refinement of Nash equilibrium in which players receive a signal, the **correlating device**, public or private, and condition their strategies on it. It coordinates without direct communication.
  - A correlating device removes three obstacles to cooperation in positive-sum games: (1) information costs, (2) transaction costs of cooperation, (3) uncertainty.
  - **Focal points** (Schelling 1960): salient choices players converge on with no signal at all (meeting at Grand Central Station).
  - **Conventions** (footnote 8): rules people consciously follow. Focal points are psychological anchors people may not be aware of.

## Key Concepts
- **Noncooperative vs cooperative game**: independent pursuit of own interest with no communication, versus joint pursuit of a common goal with communication or negotiation.
- **Kin cooperation**: apparent altruism toward relatives who share genes (worker bees, alarm calls).
- **Stable match**: no pair would both prefer each other over their current assignment.
- **Marginal contribution**: the worth a player adds to the coalition of its predecessors.
- **Value**: a function assigning a real number to every game and every player.
- **Subgame (S, υ)**: υ restricted to subsets of S.
- **Positive-sum game**: a game where players gain to the degree others cooperate.

## Mental Models
- **Use Battle of the Sexes when parties agree to act together but disagree on what to do.**
- **Use the Stag Hunt when a safe solo option competes with a better joint option that needs trust.**
- **Use the committed-cooperator matrix when going alone yields nothing.**
- **Think of a stated wish to cooperate as a probability, not a payoff.** The simulation says agents "should not cooperate if the measurable benefits do not justify it."
- **Think of the IMF as a correlating device**: two central banks barred from coordinating can each condition on its published recommendation.
- **Compare SV and MV allocations.** The gap shows how far bargaining power, not claims, drives the outcome.

## Anti-patterns
- **Treating a declared intent to cooperate as sufficient**: parties often fail to agree despite sincere desire.
- **Trusting a pressured agreement**: a party that cooperates against its interest, under pressure from mediators or counterparties, is likely to violate later. The text's case is the erosion of the GATT (signed 1947).
- **Assuming equal splits**: allocations follow initial claims, not equality.
- **Stopping at formation**: maintaining a cooperative structure matters as much as forming it.

## Reference Tables

**Table 3.1. Pure Coordination: The Driving Game**

| | Left | Right |
|---|---|---|
| **Left** | 10, 10 | 0, 0 |
| **Right** | 0, 0 | 10, 10 |

**Table 3.2. Battle of the Sexes** and **Table 3.3. Battle of the Central Banks** (same payoffs)

| | Stravinsky / ECB Hike | Khachaturian / ECB Maintain |
|---|---|---|
| **Stravinsky / Fed Hike** | 10, 5 | 0, 0 |
| **Khachaturian / Fed Maintain** | 0, 0 | 5, 10 |

**Table 3.4. Stag Hunt** (High Value context)

| | Stag | Hare |
|---|---|---|
| **Stag** | 5, 5 | -1, 3 |
| **Hare** | 3, -1 | 3, 3 |

**Table 3.6. Stag Hunt 2** (Low Value context)

| | Stag | Hare |
|---|---|---|
| **Stag** | 4, 4 | -2, 3 |
| **Hare** | 3, -2 | 3, 3 |

**Table 3.5. Evolutionarily Committed Cooperators**

| | Cooperate | Defect |
|---|---|---|
| **Cooperate** | 1, 1 | 0, 0 |
| **Defect** | 0, 0 | 0, 0 |

**Stag Hunt simulation runs** (3.3). Long-run levels are my reading of the charts on PDF pp. 75-77. The text states only which action wins.

| Run | P(High Value) | High Value Stag payoff | P(cooperate, High) | P(cooperate, Low) | Winner in text | Stag level read from chart (Hare = 3) |
|---|---|---|---|---|---|---|
| 1 (Fig 3.1) | 0.65 | 5 | 0.65 | 0.60 | Hare | about 2.7 |
| 2 (Fig 3.2) | 0.65 | 6 | 0.65 | 0.60 | Stag | about 3.2 |
| 3 (Fig 3.3) | 1.00 | 5 | 0.65 | 0.60 | Hare | about 2.75 |
| 4 (Fig 3.4) | 1.00 | 5 | 0.75 | 0.60 | Stag | about 3.5 |

**Maritime dispute: SV versus MV** (3.4, 3.5)

| Country | Claim / reservation value | SV allocation | Bargaining power | MV allocation |
|---|---|---|---|---|
| A | 55% | 22% | 0.3 | 18.97% |
| B | 65% | 26% | 0.2 | 14.94% |
| C | 55% | 22% | 0.5 | 31.61% |
| D | 75% | 30% | 0.4 | 34.48% |

## Worked Example

**1. Stag Hunt under CMAB** (3.3). Contexts: Table 3.4 (High Value Stag, probability 0.65) and Table 3.6 (Low Value Stag, probability 0.35). Player 1 cooperates with probability 0.65 if High Value and 0.60 if Low Value. The Hare pays a constant 3.
- Run 1: Hare has the higher long-run average, despite the high probabilities on both High Value and cooperation.
- Run 2: raise the High Value Stag payoff from 5 to 6, nothing else. Stag now wins.
- Run 3: instead set P(High Value) = 1. Hare still wins.
- Run 4: keep P(High Value) = 1 and raise P(cooperate given High) to 0.75. Stag wins.
- Conclusion in the text: "inducing cooperation is hard." Probabilities of cooperation must be very high to move Stag ahead, while one extra unit of payoff does it directly. The Hare's appeal is that its payoff carries no uncertainty.

**2. Maritime gas-field dispute** (3.4, 3.5). Four nations claim shares that sum to 250%. The SV gives A 22%, B 26%, C 22%, D 30%. Adding bargaining powers (A 0.3, B 0.2, C 0.5, D 0.4) and treating claims as reservation values, the MV gives A 18.97%, B 14.94%, C 31.61%, D 34.48%.
- The text's reading: bargaining power can override the ranking implied by reservation values. A gets more than B although B's reservation value is higher. Bargaining power also concentrates the outcome on C and D relative to the SV.
- Every country is allocated less than its reservation value in both solutions. The text says such a shortfall "could be an indication that the solution is unstable" but does not apply that test to this example.

**3. Alliance matching** (3.5). Three greater powers, five lesser powers, capacity two each.
- Greater-power rankings: GP1 {LP2, LP5, LP1, LP4, LP3}. GP2 {LP3, LP5, LP4}. GP3 {LP2, LP4, LP1, LP5}.
- Lesser-power rankings: LP1 {GP3, GP1, GP2}. LP2 {GP3, GP1, GP2}. LP3 {GP2, GP1, GP3}. LP4 {GP3, GP2, GP1}. LP5 {GP1, GP2, GP3}.
- Result as printed: GP1 {LP2, LP3}, GP2 {LP4}, GP3 {None}. LP1 and LP5 unmatched.
- See Extraction Notes: this printed result does not satisfy the algorithm's own stability definition.

## Key Takeaways
1. Classify a cooperative situation by structure: pure coordination, Battle of the Sexes, Stag Hunt, or committed cooperation.
2. In a Stag Hunt, raise the payoff to cooperation rather than the willingness to cooperate. Payoff moved the result more.
3. Treat agreements signed under pressure, with weak measurable benefits, as candidates for later violation.
4. Test an allocation for fairness with the SV and for stability with the MV and reservation values.
5. Derive alliance preferences from research and revealed behavior, compute the stable match, then monitor events against it.
6. Look for a correlating device (a credible institution's public signal) or a focal point when explicit coordination is barred.

## Connects To
- **Ch 1**: bounded rationality, satisficing, the Hobbesian "cooperation from necessity", Sunstein's social roles.
- **Ch 2**: PD versus SH. Table 3.5 resembles the mortar men game (footnote 5). Same CMAB and UCB machinery.
- **Ch 4**: Q-learning for games where actions change the state.
- **Ch 6**: the Shapley value returns as a judgment-aggregation tool (6.5).
- **External**: Skyrms (1996, 2004), Shapley (1953), Gale and Shapley (1962), Myerson (1977), Aumann (1974), Schelling (1960).

## Extraction Notes
- Equations 3.1 to 3.7 were undecoded in the extraction and recovered from PDF pp. 80 and 84.
- Figures 3.1 to 3.4 are image placeholders. Chart levels above are approximate readings from PDF pp. 75-77.
- Source as printed, eq. 3.1: the PDF prints "m_i^ω = (N, υ) := ...". The equals sign looks like a typesetting slip.
- Source as printed, eq. 3.4 (Symmetry) gives only the condition and omits the conclusion about φ_i and φ_j. Eq. 3.6 (Null Player) prints "υ(S ∪ Z{i})" with an unexplained "Z" and omits the conclusion that a null player receives zero. Not completed here.
- Source as printed, eq. 3.7 (Myerson value): the text describes it as a weighted average *difference* in worth with and without the player, but the printed formula has no difference term.
- The text does not state the characteristic function υ used for the maritime example. Arithmetic check (mine, not the author's): the SV figures equal each claim divided by the total claims of 250, and the MV figures equal claim times bargaining power, divided by the sum of those products (87).
- Algorithm 3.1 as printed numbers its conditions 3, 5, 4 and 6, 8, 7, uses leftover symbols M(r) and (r, h) from the hospital-resident version, and says "the preference list of l, denoted by p(g)."
- Source inconsistency, alliance example: under the printed rankings, LP2 ranks GP3 first, GP3 ranks LP2 first and GP3 is left with no partner. So (LP2, GP3) is a blocking pair for the printed result. The same holds for (LP3, GP2). The printed matching is reproduced as is.
- Table 3.2 is titled "Battles of the Sexes" in the source. The text spells the algorithm both "Gale-Shapley" and "Gale-Shapely".
