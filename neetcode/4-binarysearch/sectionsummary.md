# Section Summary — Binary Search (Neetcode)

- Focus: search invariants, edge handling, binary search on answer.

Review prompts:
- Show binary search template and common variants.
- Practice: search in rotated array, kth element problems.

## Deep-dive prompts
- Define a monotonic predicate and show how “binary search on answer” uses it.
- Choose one template: `low <= high` or `low < high` — explain your invariants.
- For rotated arrays: how do you decide which half is sorted?
- For first/last occurrence: what changes in the boundaries vs standard search?

## Mini quiz (no notes)
1) What is the invariant of binary search?
2) True/False: Binary search requires the array itself be sorted.
3) Give an example of binary searching the answer space.
4) Why is `mid = (low + high) // 2` safe in Python but can overflow in some languages?

## Operations & gotchas drill
- Template drill: write your binary search invariant in words.
- Boundary gotcha: what changes when you want first occurrence vs any occurrence?
- “Binary search on answer”: define a predicate for a sample problem (Koko, capacity, etc.).
- Rotated array: how do you detect which half is sorted and why does that help?
- Termination gotcha: show a case where `low = mid` causes an infinite loop (and the fix).
- Overflow note: why some languages use `low + (high-low)//2`.
- Debug trick: test on smallest inputs (size 0/1/2) and check updates.

### Quick quiz
1) True/False: Binary search requires a sorted array of values.
2) What does “monotonic predicate” mean?
3) For `low < high` style, what do you return at the end and why?
4) What’s the difference between `bisect_left` and `bisect_right` conceptually?
5) Give one reason off-by-one bugs happen in binary search.
6) In rotated search, what’s the key comparison you make to decide the side?
