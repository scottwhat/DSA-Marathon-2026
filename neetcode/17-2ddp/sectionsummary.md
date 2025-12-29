# Section Summary — 2D DP (Neetcode)

- Focus: DP on grids/matrices, state transitions for paths and submatrices.

Review prompts:
- When to use DP vs BFS on grids? Typical transitions.
- Practice: unique paths, edit distance, coin change 2 variants.

## Deep-dive prompts
- Define state and transition for a classic DP (coin change or LIS).
- Explain memoization vs tabulation and how to convert between them.
- Identify base cases and why missing base cases breaks correctness.
- Describe time/space optimization patterns (rolling arrays).

## Mini quiz (no notes)
1) True/False: DP always requires a table.
2) In coin change (min coins), what does `dp[i]` represent?
3) What is overlapping subproblems? Give an example.
4) When can you reduce space from O(n) to O(1)?

## Operations & gotchas drill
- State-definition drill: define state in one sentence for a DP problem you know.
- Transition drill: write the recurrence and explain each term.
- Base-case gotcha: why missing base cases silently breaks correctness.
- Memo vs tab: when is recursion+memo easier and when is tabulation safer?
- Space optimization: when rolling arrays work (dependency only on previous row/col).
- Trick: how do you detect whether DP is overkill (subproblems don’t overlap)?
- Debug trick: print small dp tables for tiny inputs.

### Quick quiz
1) True/False: DP always improves time complexity.
2) What does `dp[i]` typically mean in 1D DP?
3) In 2D DP, what does `dp[r][c]` usually represent?
4) Give one example of unbounded knapsack.
5) What is “optimal substructure”?
6) Why can LIS be done in O(n log n) (high-level)?
