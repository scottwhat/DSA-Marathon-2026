# Section Summary — Heaps / Priority Queues

- Core concepts: heap operations, using heaps for k-largest/k-smallest, merging sorted streams.
- Key patterns: maintain top-k, sliding window medians, Dijkstra priority queue usage.
- Implementation tips: Python `heapq` is min-heap; invert values for max-heap behavior.

Review prompts:
- When to use heap vs sorting vs BST for top-k problems?
- How to merge k sorted lists with a heap; complexity analysis.
- Practice: top-k frequent elements, kth largest, median from data stream (conceptual).

## Deep-dive prompts
- Explain min-heap vs max-heap and how to simulate max-heap in Python.
- For top-k: when do you keep a size-k heap vs pushing everything?
- For merging k sorted lists: what do you store in the heap and why?
- Contrast heap approach vs quickselect for kth element.

## Mini quiz (no notes)
1) What are the complexities of `push` and `pop` on a binary heap?
2) True/False: A heap is fully sorted.
3) If you keep a min-heap of size k for kth largest, what do you pop when size exceeds k?
4) Why do you need a tie-breaker field when heap items can compare equal?

## Operations & gotchas drill
- Heap ops: insert/pop complexities and why.
- Gotcha: Python `heapq` is a min-heap—how do you simulate a max-heap?
- Top-k pattern: maintain size-k heap; explain what gets popped and why.
- Tie-breaker gotcha: why tuples sometimes need an extra field to compare safely.
- K-way merge: what exactly is stored (value + source pointer) and what happens after pop.
- Alternative: when is quickselect better than a heap?
- Dijkstra link: why is a heap used there and what does it store?

### Quick quiz
1) True/False: A heap gives O(1) access to the maximum element (in a min-heap).
2) What’s the difference between heap and balanced BST for top-k queries?
3) In k closest points, what is the heap key?
4) Why is “push all then pop k times” sometimes worse than “size-k heap”?
5) What does “heap invariant” mean?
6) When merging k sorted lists, what is the time complexity in terms of N and k?
