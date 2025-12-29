# Section Summary — Sliding Window (Neetcode)

- Focus: dynamic windows, maintaining counts and results.

Review prompts:
- How to convert a problem into a sliding-window formulation?
- Practice: minimum window substring, longest substring without repeating characters.

## Deep-dive prompts
- Give the generic skeleton for variable-length windows (expand, validate, shrink, update answer).
- When do you update the answer: before shrinking, after shrinking, or both?
- Name 3 window states you might track (counts, sum, distinct count, max frequency) and how you update them.
- Explain why many window solutions are O(n) even with nested loops.

## Mini quiz (no notes)
1) Fixed vs variable window: which one fits “max average subarray of length k” and why?
2) True/False: A correct window algorithm never moves `left` backward.
3) In “minimum window substring”, what makes a window “valid”?
4) What is the most common bug in window problems?

## Operations & gotchas drill
- Fixed vs variable: name a problem that is fixed window and one that is variable window.
- State maintenance: list 4 window states you might track and the update rules.
- Validity checks: how do you avoid O(n) rescans inside the window?
- Gotcha: when shrinking, what do you update first (state, left pointer, answer)?
- Complexity proof: explain why nested loops can still be O(n) in a correct window.
- Trick: when does “max frequency in window” allow you to avoid shrinking too aggressively?
- Counterexample drill: build an example that breaks a naive window approach.

### Quick quiz
1) True/False: Window problems can always be solved by sorting first.
2) What’s the main difference between “minimum window” and “maximum window” problems?
3) In min-window-substring, what does it mean to be “valid”?
4) Why is moving `left` forward safe once the window is valid?
5) What’s the classic bug with window length calculation?
6) When do you use a deque in sliding window problems?
