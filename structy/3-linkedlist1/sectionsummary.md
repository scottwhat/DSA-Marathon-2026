# Section Summary — Linked List (Structy)

- Focus: pointers, insertion/removal, reversal, middle and kth-from-end.

Review prompts:
- Explain in-place reversal and two-pointer for middle/kth-from-end.
- Practice: remove node, zip lists, merge lists.

## Deep-dive prompts
- List the “pointer safety checks” you do before dereferencing `node.next`.
- Walk through reversing a list: what pointers do you need and what changes each step?
- For merging lists, explain dummy head usage and why it reduces bugs.
- Explain Floyd’s cycle detection and how to find the cycle entry.

## Mini quiz (no notes)
1) What’s the difference between reversing a list and reversing nodes in k-group?
2) True/False: You can detect a cycle using a hash set in O(n) space.
3) What edge cases commonly break linked list code (name 4)?
4) In copy-random-pointer, what does the hashmap map from and to?

## Operations & gotchas drill
- Core ops: insert/delete at head, tail, and middle — what are their time costs and why?
- Dummy head trick: why does it reduce edge-case bugs?
- Reversal drill: list the exact pointer updates per step (`prev`, `cur`, `nxt`).
- Cycle detection: compare hash-set visited vs Floyd (space/time tradeoff).
- Gotcha: why do “kth from end” solutions often use a gap between pointers?
- Merge trick: why is a `tail` pointer useful even if you have `head`?
- Mutation gotcha: what happens if you accidentally reuse nodes from the original list in multiple lists?
- Copy random pointer: what does the mapping represent and what’s the second-pass fixup?

### Quick quiz
1) True/False: Accessing the ith element of a linked list is O(1).
2) What is the most common bug when deleting a node (pointer order)?
3) Why does using a dummy head simplify removing the first node?
4) In reversing, what does `cur.next = prev` accomplish?
5) What’s a safe way to handle “empty list” and “single node” cases?
6) When merging lists, how do you avoid losing the remaining nodes?
