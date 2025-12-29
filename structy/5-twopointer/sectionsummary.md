# Section Summary — Two Pointer (Structy)

- Focus: sliding windows and paired-pointer solutions on arrays/strings.

Review prompts:
- Demonstrate two-pointer approach for palindrome checks and compression.
- Practice: uncompress/compress, is-palindrome.

## Deep-dive prompts
- For left/right pointers: what is the decision rule to move left vs right?
- For fast/slow pointers: what property are you detecting (cycle, middle, kth-from-end)?
- Explain how to avoid duplicates in 3Sum after sorting.
- Derive the two-pointer solution for trapping rain water (why max-left/max-right works).

## Mini quiz (no notes)
1) In a sorted array, how do you find two numbers summing to target in O(n)?
2) Why does Floyd’s cycle algorithm detect a cycle?
3) For “container with most water”, why can you move the shorter side pointer safely?
4) True/False: Two pointers always require the array be sorted.

## Operations & gotchas drill
- For left/right pointers, write the decision rule you use to move pointers in sum/partition problems.
- What invariants must hold for two pointers to be correct in a sorted array?
- Duplicate-handling gotcha: how do you avoid duplicate triplets in 3Sum?
- Partition trick: explain the “read pointer vs write pointer” pattern.
- Fast/slow pointer drill: identify which problems need cycle detection vs middle vs intersection.
- Edge-case drill: even vs odd length lists/arrays — where do slow/fast end?
- Trapping rain water: explain why the lower side determines trapped water locally.
- When two-pointers fails: give an example where it seems applicable but isn’t (and what to use instead).

### Quick quiz
1) True/False: Two pointers always gives O(n) time.
2) In `container with most water`, why can you discard the shorter side?
3) What’s the standard way to remove duplicates in-place from a sorted array?
4) When using fast/slow on linked lists, what null checks prevent crashes?
5) Give one example of two pointers without sorting.
6) What’s the main gotcha when using two pointers on strings (immutability)?
