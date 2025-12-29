# Section Summary — Bit Manipulation (Neetcode)

- Focus: bitwise ops, masking, parity, lowbit tricks, XOR properties.

Review prompts:
- Common tricks: isolate lowest set bit, count bits, swap using XOR.
- Practice: single-number variants, missing number, reverse bits.

## Deep-dive prompts
- Explain XOR properties used in single-number and missing-number problems.
- Show how to check/set/clear/toggle the kth bit.
- Explain `n & (n - 1)` and what it does.

## Mini quiz (no notes)
1) What does XOR of a number with itself produce?
2) True/False: `n & (n - 1)` clears the lowest set bit.
3) How do you test if the kth bit is set?
4) Why can missing number be solved with XOR?

## Operations & gotchas drill
- Core ops: AND/OR/XOR/SHIFT — what does each do conceptually?
- XOR trick: why XOR cancels pairs.
- Lowbit trick: explain `n & (n - 1)` and when to use it.
- Shift gotcha: operator precedence pitfalls in some languages (be explicit with parentheses).
- Signed vs unsigned gotcha: why bit problems differ between languages.

### Quick quiz
1) True/False: `x ^ x == 0`.
2) How do you check if the kth bit is set?
3) What does `n & -n` represent?
4) Why does XOR help find a unique element when others appear twice?
5) How do you count set bits efficiently?
