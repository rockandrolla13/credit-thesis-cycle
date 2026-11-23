# Chapter 2: The Constraint Framework: Three Pillars

## Core Idea
Make market calls "based not on what policymakers want to do, but on what they must do given their material reality". Three pillars support this: the materialist dialectic, diagnosticity, and the person-versus-situation finding from social psychology. A short probability model formalizes it.

## Frameworks Introduced
- **The Maxim That Shall Forever Be Bolded**: "Preferences are optional and subject to constraints, whereas constraints are neither optional nor subject to preferences."
- **The three pillars** (the author's own review list):
  1. **The Materialist Dialectic** (philosophical; from Marx). Start analysis in the material world, not the world of ideas. Seek "the immutable reality - the constraints - in a situation". The economic constraint is not always the most important, but "some other tangible barrier will be".
  2. **Diagnosticity** (practical; from Richards Heuer, *Psychology of Intelligence Analysis*). Information is scarce and poor, so use data with high diagnosticity to falsify hypotheses. "Policymakers' preferences are not diagnostic. Constraints are."
  3. **Social Psychology** (empirical; from Ross and Nisbett, *The Person and the Situation*). Context and situation drive behaviour, not the person. Avoid the fundamental attribution error.
- **The five material constraints, in the author's stated order "from the most salient to the least"**: *political*, *economic*, *financial*, *geopolitical*, *constitutional/legal*. Then "the constraint wild cards: terrorists and pandemics".
  - Note on the source: this sentence lists economic and financial separately, yet Part Two treats them in one chapter (Ch 5, "The Economy and the Market"). Ch 8 covers the wild cards under the heading of the time constraint.
- **"When something blows up, buy everything"**: the author's reply to those who use geopolitics only as an event hedge. "Other than the 1973 Yom Kippur War, few geopolitical events since the Second World War have been disastrous for the markets" (Figure 2.1).
- **Preference analysis is a one-off, constraint analysis is iterative**: a biography or history book is "always the first place to start". Do it "once or twice per public figure". Then track constraints.

## The formal model (recovered from PDF pp. 59-62; book pp. 39-42)
The extraction lost all three equations. They read as follows on the page.

**Preference model.** Decision-maker X, preferred outcome Y:

    P(Y) = p_X(y) · p_y(Y)

- p_X(y): probability that X prefers action y.
- p_y(Y): probability that taking action y leads to outcome Y.

**Constraint model.** Add constraining variables Z:

    P(Y) = Σ_Z  p_X(y|Z) · p_y(Y|Z) · p_Z(Z)

- p_Z(Z): probability that Z is true and affects the outcome.
- The two models give the same P(Y) only when constraints are irrelevant ("Z = 0, or the total constraints have zero influence"), under p_X(y) = Σ_Z p_X(y|Z) and p_y(Y) = Σ_Z p_y(Y|Z).

**NBA "hold me back" instance** (as printed, including its punctuation):

    P(Y) = Σ_{Z=0,1} p_X(y|Z) · p_y(Y|Z)
         = p_X(y|Z=0) · p_y(Y|Z=0) + p_X(y|Z=1) · p_y(Y|Z=1)
         = 0

- Z = 1 means teammates are nearby. p_X(y|Z=1) = 1 and p_y(Y|Z=1) ≈ 0.
- Z = 0 means no teammates nearby. p_X(y|Z=0) = 0 and p_y(Y|Z=0) = 1.
- Both terms are zero. "The preference to fight is anticorrelated with the probability of a fight outcome."
- Geopolitical reading: leaders taunt and signal aggression precisely when something will hold them back. Rhetoric may even aim to bring the opponent back to the table.

Source inconsistencies to keep in mind (recorded, not corrected):
- The preference-model bullet says the final outcome "is rarely a fight. So P(Y) ≈ 1". The surrounding logic implies P(Y) ≈ 0.
- The NBA equation omits the p_Z(Z) weight that the general constraint model includes.
- The author says the model was written by physicist Dan Green and is there to "fill the required quota". Treat it as illustration, not as an estimation method.

## Key Concepts
- **Fortuna / Virtù**: Machiavelli's fate versus the Prince's skill. The forecast "must start with" the course of Fortuna. The policymaker's reaction "is a derivative of the flood".
- **Materialist dialectic**: material conditions create human reality. Thought systems are a derivative. "People cannot 'think' or 'prefer' their way out of material constraints."
- **Diagnosticity**: Heuer's term, "the extent to which any item of evidence helps the analyst determine the relative likelihood of alternative hypotheses". A fever above 38°C has low diagnostic value because it fits many illnesses.
- **Competing hypotheses analysis**: using diagnostic evidence to eliminate hypotheses. A nondiagnostic variable eliminates none.
- **Fundamental attribution error**: attributing outcomes to actors' character, personality and mood instead of the external context.
- **Debt Supercycle**: BCA Research's term (Tony Boeckh, early 1970s) for post-war reliance on private-sector relevering. The author says it "didn't end until 2008" and is "a deeply political concept".
- **Herb Stein's law**: "if something cannot go on forever it will stop."

## Mental Models
- Think of Fortuna as ale poured down a hill. If you know the terrain you can predict the flow. Constraints are the terrain.
- Use constraints as "gatekeepers that determine whether preferences affect the outcome".
- More information raises conviction, not necessarily accuracy (Heuer). Ask which datum would eliminate a hypothesis.
- Each decade's macro theme has "an unspoken geopolitical anchor". The author's reading of BCA's archive:
  - 1945-1961: five recessions, policymakers rely on private relevering → Debt Supercycle.
  - 1960s: complacency on inflation, Vietnam plus Great Society, deficits soar outside recession. "In 2020, we are living in a 1960s rerun."
  - 1970s: stagflation caused mainly by 1960s demand-side choices. The 1973 oil crisis is "the rare example of a significant geopolitical Black Swan".
  - 1980s: political revolution, supply-side policy, central banks with a popular mandate to crush inflation.
  - 1990s: Soviet collapse plus supply-side revolution → globalization and US hegemony → Great Moderation.
  - 2000s: Debt Supercycle reinflated after 9/11. Inequality drives household levering-up (Figure 2.2).

## Anti-patterns
- **Geopolitics as a Black Swan desk**: writing a piece "every time something blows up" makes the analyst an appendage and adds a random risk to someone else's view.
- **Reading preferences from rhetoric**: you cannot gauge sincerity, commitment or pain threshold.
- **Personalized news narratives**: media tell human stories. "Geopolitical analysts have no such excuse."
- **False precision from formal theory**: formal expression "produces knowledge without the particulars of context".

## Reference Tables

### The Princeton Seminary experiment (Darley and Batson, early 1970s)
Seminary students prepared a sermon on the Good Samaritan, then passed a person needing help.

| Time condition | Share who stopped to help |
|---|---|
| Very late, superiors already waiting | 10% |
| Would be late if they did not leave soon | 45% |
| No rush | 63% |

Reading: preference to help was as strong as it gets and was primed. The time constraint still dominated.

### Three fundamental-attribution-error cases

| Narrative | Date in text | Constraints the author cites | What happened, per text |
|---|---|---|---|
| "Kim Jong-un Is a Wild Card" | early 2013; again 2017 | Limited ballistic missile technology in 2013. Paltry conventional forces apart from artillery. China opposes confrontation because it would bring more US forces. Seoul is exposed to artillery, so the South must pre-empt, which ends the Kim dynasty. | No war. In 2017 "the White House bluff ultimately worked" because Kim "was never holding a strong hand". |
| "Israeli Hawks Want to Bomb Iran" | since 2011; oil risk premium in early 2012 | Israel has no strategic bomber force. Syrian civil war and Islamic State were more proximate threats. Fordow went fully operational in December 2011, making Iran "an implied nuclear power"; a strike would guarantee an eventual device. | No strike is described. |
| "Vladimir Putin Wants to Recreate the Soviet Union" | after 2008 Georgia, 2014 Crimea | At least 80% of Russian gas exports went to the EU in 2019, about half of that to Germany. "It is actually Berlin that has Russia by the … pipelines." Russia's military lacks power projection; it "barely had the capacity to intervene in Donbas". Gas infrastructure to China takes over a decade. | The author treats "the Baltics are next" as the error. |

### Figure 2.1: S&P 500 after geopolitical events (recovered from PDF p. 41; book p. 21)
"If something blows up, just close your eyes and buy." The full table as printed. Blank cells on the page are shown as n/a.

| Event | Date | Max S&P 500 decline* | 1 month later | 3 months later | 6 months later | 12 months later |
|---|---|---|---|---|---|---|
| Hungarian Revolution | 1956-10-23 | -10.78% | -2.12% | -2.71% | -1.02% | -11.69% |
| Cuban Missile Crisis | 1962-10-16 | -10.52% | 5.40% | 13.30% | 21.13% | 27.84% |
| Prague Spring | 1968-01-05 | -10.04% | -4.24% | -2.76% | 5.18% | 8.39% |
| Tet Offensive | 1968-01-30 | -9.31% | -3.80% | 5.06% | 5.22% | 10.40% |
| Nixon Shock | 1971-08-15 | -9.38% | 4.26% | -4.05% | 9.76% | 17.11% |
| Yom Kippur War/1st Oil Shock | 1973-10-06 | -16.10% | -4.45% | -9.97% | -15.33% | -43.25% |
| Iranian Revolution/2nd Oil Shock | 1979-01-16 | -6.32% | -0.79% | 1.67% | 3.30% | 11.65% |
| Soviet Invasion of Afghanistan | 1979-12-25 | -10.86% | 5.53% | -7.87% | 8.42% | 26.21% |
| Tiananmen Square Massacre | 1989-06-04 | -2.32% | -1.93% | 8.67% | 7.95% | 12.87% |
| Berlin Wall Collapse | 1989-11-09 | -10.23% | 3.60% | -0.88% | 1.87% | -6.78% |
| Gulf War 1 | 1990-08-02 | -19.92% | -8.23% | -11.28% | -2.40% | 10.16% |
| Coup Against Gorbachev | 1991-08-19 | -3.62% | 2.95% | 0.78% | 8.44% | 11.08% |
| Dissolution of USSR | 1991-12-26 | -0.23% | 2.63% | 0.75% | -0.34% | 8.63% |
| US Bombing of Chinese Embassy In Belgrade | 1999-05-07 | -5.97% | -0.78% | -3.32% | 1.88% | 6.52% |
| US-China P3 Incident | 2001-04-01 | -19.69% | 9.14% | 5.52% | -10.50% | -1.19% |
| 9/11 | 2001-09-11 | -23.10% | 0.45% | 4.05% | 6.93% | -16.76% |
| George W Bush UN speech | 2002-09-12 | -25.11% | -5.82% | 1.66% | -9.33% | 14.85% |
| Operation Iraqi Freedom/Gulf War 2 | 2003-03-20 | -8.96% | 2.05% | 13.71% | 18.34% | 26.73% |
| Madrid terrorist attack | 2004-03-11 | -6.36% | 2.94% | 2.68% | 1.55% | 8.43% |
| Ukraine Orange Revolution | 2004-11-22 | -1.72% | 2.75% | 0.59% | 1.02% | 7.13% |
| London terrorist attack | 2005-07-07 | -2.09% | 2.38% | -0.16% | 7.31% | 5.64% |
| Lebanon War | 2006-07-12 | -6.88% | 0.65% | 8.28% | 13.68% | 22.97% |
| First North Korean nuclear test | 2006-10-09 | -0.24% | 2.05% | 4.55% | 6.96% | 15.88% |
| Lehman Collapse | 2008-09-15 | -44.68% | -23.88% | -27.18% | -36.57% | -11.74% |
| India Mumbai attacks | 2008-11-26 | -42.85% | -1.68% | -15.19% | 2.55% | 25.12% |
| EU Debt Crisis | 2010-01-13 | -7.87% | -6.12% | 4.51% | -4.39% | 12.05% |
| ROKS Cheonan sinking | 2010-03-26 | -10.54% | 3.90% | -7.70% | -1.54% | 12.62% |
| Senkaku rare earth embargo | 2010-09-08 | -2.56% | 6.03% | 11.78% | 20.29% | 7.92% |
| Arab Spring (Mubarak steps down in Egypt) | 2011-02-11 | -5.44% | -1.87% | 0.97% | -11.78% | 1.01% |
| NATO intervention Libya | 2011-03-19 | -5.78% | 2.61% | -0.60% | -5.87% | 10.21% |
| US Debt Ceiling 2011 | 2011-08-02 | -19.25% | -6.39% | -1.29% | 5.70% | 8.85% |
| Netanyahu red line on Iran | 2012-09-27 | -7.67% | -2.43% | -2.01% | 8.00% | 16.90% |
| US Fiscal 2013 | 2013-01-01 | -2.41% | 6.10% | 9.53% | 13.24% | 29.60% |
| Ghouta, Syria chemical attack | 2013-08-21 | -4.63% | 4.09% | 9.32% | 11.78% | 21.28% |
| Debt Ceiling and Government Shutdown | 2013-10-01 | -4.06% | 3.93% | 9.05% | 11.24% | 14.82% |
| China ADIZ East China Sea | 2013-11-23 | -3.48% | 1.29% | 1.74% | 5.31% | 14.34% |
| Crimean Invasion | 2014-02-27 | -2.08% | -0.28% | 3.11% | 7.86% | 13.49% |
| Islamic State (Fall of Mosul) | 2014-06-04 | -0.95% | 2.99% | 3.62% | 7.47% | 8.71% |
| Greek bailout referendum | 2015-07-05 | -12.35% | 1.11% | -4.32% | -2.89% | 0.57% |
| Russian intervention into Syria | 2015-09-30 | -9.78% | 8.30% | 7.46% | 7.50% | 12.93% |
| Paris Terrorist Attacks | 2015-11-13 | -13.31% | -0.53% | -7.82% | 1.17% | 6.99% |
| North Korean Nuclear Test | 2016-01-06 | -13.31% | -5.54% | 3.84% | 5.50% | 14.41% |
| BREXIT Referendum | 2016-06-23 | -5.60% | 2.92% | 2.43% | 7.12% | 15.38% |
| North Korean Nuclear Test | 2016-09-09 | -4.79% | 1.22% | 6.19% | 11.14% | 15.68% |
| Trump's election | 2016-11-08 | -2.31% | 4.98% | 7.25% | 12.14% | 21.26% |
| Hwasong-14 North Korean Test | 2017-07-04 | -1.78% | 1.97% | 4.48% | 12.14% | 11.70% |
| Trump declares trade war | 2018-03-01 | -10.13% | -1.37% | 2.13% | 8.36% | 4.71% |
| US-China trade war escalates | 2018-05-29 | -3.47% | 1.06% | 8.33% | 1.78% | 3.46% |
| US sanctions on Iran | 2019-05-02 | -6.84% | -5.67% | 0.50% | 5.12% | -2.98% |
| US-China trade war escalates | 2019-08-01 | -6.12% | -0.92% | 3.84% | 9.21% | 10.75% |
| Iran strikes Saudi refinery | 2019-09-14 | -4.57% | -1.37% | 5.37% | -9.85% | n/a |
| US strikes Iran's Soleimani | 2020-01-03 | -31.32% | 0.43% | -23.07% | -3.24% | n/a |
| Coronavirus Outbreak | 2020-01-20 | -32.80% | 1.31% | -15.21% | -2.34% | n/a |
| Russia-Saudi Oil Price War | 2020-03-08 | -33.92% | -7.48% | 8.75% | n/a | n/a |
| **Mean gain/loss** |  | -10.67% | 0.06% | 0.70% | 3.51% | 9.46% |
| **Median gain/loss** |  | -7.28% | 1.09% | 1.94% | 5.31% | 10.92% |

*Table note as printed: returns are calculated based on peak-to-trough market drawdowns around the cited events for a maximum window of three months before and after each event. Source line: BCA Research.

Reading the table: 54 events from 1956 to 2020. Mean and median 12-month returns are positive (9.46% and 10.92%). The Yom Kippur War row (-43.25% at 12 months) is the outlier the author names. Other negative 12-month rows on the page: Hungarian Revolution, Berlin Wall collapse, US-China P3 incident, 9/11, Lehman collapse and the 2019 US sanctions on Iran.

## Worked Example: Obamacare repeal (2017)
1. **Preference**: Trump and the Republican party clearly wanted repeal. By summer 2017 Republicans had tried to kill the Act 70 times since 2010.
2. **Why the preference is not diagnostic**: sincerity and pain threshold are unknowable. The Act is an entitlement, and the US record of repealing entitlements is poor.
3. **Constraints**: (a) risk of losing popular support, and (b) congressional math. The Senate majority was thin. Reconciliation removed the filibuster but not the need for moderate votes.
4. **Outcome**: the repeal bill failed 49-51 in the Senate. Collins, Murkowski and McCain could not be wished away. Support for the Act rose in mid-2017 and surged before the 2018 midterms (Figure 2.4).
5. **Lesson**: investors were surprised because they overweighted preference. Popular support "became a material constraint".

## Key Takeaways
1. Start with the terrain. The policymaker's action is a derivative of it.
2. Rank evidence by its power to eliminate hypotheses. Preferences eliminate nothing because acting on them is optional.
3. Even highly competent policymakers succumb to material reality, and incompetent ones are "ultimately pushed to do the right thing by the constraints of the market, economics, and politics".
4. Aggressive rhetoric often signals the presence of a restraint, not its absence.
5. Do not run geopolitics as an event hedge. Median 12-month S&P 500 return after the listed events was positive.
6. The framework "is not scientific or quantitative". The author repeats this caveat on purpose.

## Extraction Notes
- All three equations were `formula-not-decoded` and are recovered from the PDF as shown above.
- Figure 2.1 was scrambled in the extraction: digits and letters were split, several rows were merged or misaligned, and the "Paris Terrorist Attacks" row (2015-11-13) was dropped. The table above replaces it and is taken from the PDF page (its text layer, with rows from 2006 to 2019 and the mean and median rows also checked against the page image). The mean and median rows match the values first read from the extraction.
- Figures 2.2 (middle-class goods inflation), 2.3 (profit share versus labor share) and 2.4 (Obamacare support) are image placeholders with captions only.

## Connects To
- **Ch 4-8**: one chapter per constraint, in the order of salience given here.
- **Ch 3**: the rival "intelligence" framework.
- **Ch 9**: diagnosticity reappears as the search for the fulcrum constraint, and probabilities are updated in a Bayesian way.
- **Ch 10**: "hold me back" rhetoric versus real game structure.
