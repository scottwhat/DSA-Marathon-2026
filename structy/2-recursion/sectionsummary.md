# Section Summary — Recursion (Structy)

- Focus: recursion base case, building up results, recursion depth tradeoffs.

Review prompts:
- Outline steps to convert recursion to iterative where necessary.
- Practice: factorial, fibonacci (memo vs iterative), tree recursion basics.

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
- Pick the top 3 data structures you’d try first and justify each.
- Identify 5 edge cases you test by default.
- List 3 invariants you could track to prove correctness.

### Quick quiz
1) True/False: Most bugs are edge-case related.
2) What is an invariant and why does it matter?
3) Give one example of trading space for time.
