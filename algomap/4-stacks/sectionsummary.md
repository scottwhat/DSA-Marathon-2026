# Section Summary — Stacks

- Core concepts: LIFO behavior, using stacks for parsing, backtracking, and monotonic stacks.
- Key patterns: parentheses validation, evaluate RPN, next greater element (monotonic stack), DFS recursion elimination.
- Implementation tips: use list as stack in Python, track indices when using monotonic stacks.

Review prompts:
- When choose stack vs recursion for DFS? Conversion tips.
- Explain monotonic stack and its typical applications.
- Practice: valid parentheses, daily temperatures, evaluate RPN.

## Deep-dive prompts
- Distinguish “simulation stack” vs “monotonic stack”; give a signature problem for each.
- What does the stack store: values, indices, or pairs (value, count)? Why?
- For monotonic stacks, define the invariant (increasing/decreasing) and the pop condition.
- Explain how to convert recursion DFS to an explicit stack.

## Mini quiz (no notes)
1) For next-greater-element style problems, why do we store indices?
2) True/False: A monotonic stack can solve daily temperatures in O(n).
3) In valid parentheses, what exactly is pushed and popped?
4) What is the time complexity of pushing/popping each element at most once?

## Operations & gotchas drill
- Stack ops drill: what are push/pop/peek complexities in Python using list?
- Valid parentheses: what exactly is stored on the stack and what is the failure condition?
- Monotonic stack gotcha: why store indices instead of values?
- Monotonic invariant: define it precisely for “next greater element” style problems.
- Amortized analysis: why is monotonic stack O(n) even with nested while-loops?
- Parsing trick: how do you handle multi-digit numbers / tokens (e.g., RPN) safely?
- DFS conversion: when converting recursion to an explicit stack, what state must you store?
- Gotcha: when is recursion depth a problem in Python and what do you do instead?

### Quick quiz
1) True/False: A stack can be implemented with a queue in O(1) worst-case per op.
2) What is a “sentinel” value and when does it help in stack problems?
3) Why does each element get popped at most once in a monotonic stack?
4) In daily temperatures, what do you compute when popping an index?
5) What’s the difference between stack and deque in Python use-cases?
6) Name 2 problems where a stack simulates recursion.
