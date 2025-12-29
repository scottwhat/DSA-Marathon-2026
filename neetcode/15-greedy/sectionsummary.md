# Section Summary — Greedy (Neetcode)

- Focus: greedy choice property and proving correctness, sorting heuristics.

Review prompts:
- How to argue greedy correctness? Example strategies.
- Practice: jump game, gas station, partition labels.

## Deep-dive prompts
- Define “greedy choice property” and how you justify it.
- Show a counterexample mindset: what would break the greedy choice?
- Common greedy tools: sorting, two pointers, priority queues.

## Mini quiz (no notes)
1) True/False: Greedy algorithms are always optimal.
2) In jump game, what does the “farthest reachable” variable represent?
3) In gas station, why can you reset the start index when tank goes negative?
4) What kind of proof do you give for greedy correctness?

## Operations & gotchas drill
- Greedy proof drill: what’s the exchange argument in plain English?
- Counterexample drill: how do you test whether a greedy choice might fail?
- Sorting trick: many greedy solutions rely on sorting—what property does sorting create?
- Jump game: define the invariant behind tracking farthest reach.
- Gas station: why can you discard earlier start indices after tank dips negative?

### Quick quiz
1) True/False: Greedy always works if it feels right.
2) What is the difference between local optimal and global optimal?
3) Give one standard way to prove greedy correctness.
4) In interval scheduling, what is the greedy choice?
5) Name a greedy problem that is actually DP if constraints change.
