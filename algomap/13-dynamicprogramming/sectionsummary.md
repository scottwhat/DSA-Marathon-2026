# Section Summary — Dynamic Programming

- Core concepts: overlapping subproblems, optimal substructure, memoization vs tabulation.
- Key patterns: knapsack/frequency, LIS, DP on strings, DP on trees/grids, state definition and transitions.
- Implementation tips: define state clearly (index + extra parameters), start with recursion+memo then convert to iterative.

Review prompts:
- How to identify DP: ask whether subproblems overlap and can be reused.
- Show steps to convert recursive memo solution to bottom-up DP.
- Practice: coin change, longest increasing subsequence, house robber variations.

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
