# Section Summary — Dynamic Programming (Structy)

- Focus: state definition, memoization, bottom-up approaches.

Review prompts:
- How to identify overlapping subproblems; examples of state definitions.
- Practice: array stepper, counting change, longest path variants.

## Deep-dive prompts
- Define DP state and transition for one of: coin change, LIS, or grid paths.
- Compare memoization vs tabulation; explain how you’d convert a memo solution to bottom-up.
- List common DP families: 0/1 knapsack, unbounded knapsack, interval DP, DP on strings.
- Explain how to choose dimensions of state (index, remaining capacity, previous choice, etc.).
- Space optimization: when can you reduce from O(n) to O(1) or O(k) using rolling arrays?

## Mini quiz (no notes)
1) What does “overlapping subproblems” mean? Give a concrete example.
2) True/False: If subproblems don’t repeat, DP usually isn’t the right tool.
3) In coin change (min coins), what does `dp[i]` represent?
4) For LIS, what is an O(n log n) idea at a high level (no code)?

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
