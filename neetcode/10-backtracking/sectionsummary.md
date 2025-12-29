# Section Summary — Backtracking (Neetcode)

- Focus: recursion with branching and pruning; state restoration.

Review prompts:
- Explain backtracking skeleton and pruning strategies.
- Practice: N-queens, permutations, combination-sum approach.

## Deep-dive prompts
- Write a generic backtracking template: choose → explore → un-choose.
- Identify state variables and constraints; explain how pruning works.
- Compare permutations vs combinations vs subsets; how does the recursion tree differ?
- Explain how to avoid duplicates (sorting + skip rule).

## Mini quiz (no notes)
1) True/False: Backtracking is usually exponential time.
2) What does “pruning” mean in backtracking?
3) For subsets, what are the two choices at each element?
4) For word search, what is the purpose of marking visited and restoring it?

## Operations & gotchas drill
- Backtracking skeleton: choose → explore → un-choose. What exactly is “un-choose”?
- Duplicate gotcha: how do you prevent repeated combinations/permutations?
- Constraint ordering: why does checking constraints early prune more?
- Complexity drill: estimate runtime using branching factor × depth.
- State bug: what happens if you reuse the same list without copying at the right time?
- Grid DFS gotcha: why must you restore visited state when backtracking?
- Trick: when do you pass an index forward to avoid permutations when you want combinations?

### Quick quiz
1) True/False: Backtracking can often be written iteratively without any stack.
2) What’s pruning? Give one example of a pruning rule.
3) For subsets, how many total subsets exist for n elements?
4) What’s the difference between combinations and permutations in recursion structure?
5) In word search, what makes a partial path invalid?
6) Why is sorting helpful before backtracking in “subsets II”?
