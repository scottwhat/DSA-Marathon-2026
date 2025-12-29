# Section Summary — Arrays & Hashing (Neetcode)

- Core concepts & patterns: two-sum hash lookup, frequency counting, sliding window for substrings.

Review prompts:
- Why use hashing for two-sum and anagram grouping?
- Practice: two-sum, group anagrams, product except self.

## Deep-dive prompts
- Define the exact invariant you maintain in a two-pointer solution (what stays true after each move?).
- For sliding window problems: what is the window state, how is it updated, and what condition triggers shrinking?
- Compare prefix sums vs running sums vs difference arrays; when does each apply?
- Explain in-place vs out-of-place transformations; list typical pitfalls (overwriting needed data).
- For string problems: when is sorting acceptable vs frequency counting vs rolling hash?

## Mini quiz (no notes)
1) If you need to answer many range-sum queries on a static array, what preprocessing do you do and what is query time?
2) In `product of array except self`, why do two passes work and why isn’t division allowed?
3) Name 3 common off-by-one mistakes in substring/window problems.
4) Given a sorted array and target, describe how you’d find the first occurrence (not just any).
5) True/False: Rotating an $n\times n$ matrix 90° in-place is always possible without extra memory.

## Operations & gotchas drill
- What are the time complexities of: index access, append, pop-last, insert at front, delete at middle (Python list)?
- Explain amortized O(1) append: what triggers a resize and what does “amortized” mean?
- When you need O(1) membership tests, why is a list the wrong structure?
- What breaks in two-pointer code when you forget the array must be sorted (or monotonic)?
- Sliding window gotcha: when do you update the answer relative to shrinking (give a concrete example)?
- Off-by-one drill: for substring windows, list 3 different meanings of `right` (inclusive vs exclusive) and why mixing them breaks code.
- In-place gotcha: if you overwrite while iterating, how do you avoid losing data (two-pass, reverse iteration, extra buffer)?
- String gotcha: why is concatenating in a loop often slow; what’s the typical fix?
- Prefix-sum gotcha: why do many subarray-count problems need a map of prefix sums (not just a running sum)?
- Sorting trick: when does sorting enable a linear two-pointer scan vs hashing?

### Quick quiz
1) If you need to repeatedly add/remove from the front, what Python structure is better than list and why?
2) True/False: `list.pop(0)` is O(1).
3) What does “stable sort” mean and when might it matter?
4) Give one problem where sorting increases time but simplifies logic enough to be worth it.
5) In a variable-length sliding window, can `left` ever move backward? Why?
6) What is the most common mistake when computing window length?
7) True/False: Prefix sums only help for range-sum queries.
8) If you must keep relative order and remove elements in-place, what pattern do you use?
