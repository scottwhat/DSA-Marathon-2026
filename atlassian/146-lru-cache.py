# https://leetcode.com/problems/lru-cache/
# https://www.youtube.com/watch?v=7ABFKPK2hD4






# class Node:
#     def __init__(self, key, val):
#         self.key, self.val = key, val
#         self.prev = self.next = None


# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = {}  # map key to node

#         self.left, self.right = Node(0, 0), Node(0, 0)
#         self.left.next, self.right.prev = self.right, self.left

#     # remove node from list
#     def remove(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next, nxt.prev = nxt, prev

#     # insert node at right
#     def insert(self, node):
#         prev, nxt = self.right.prev, self.right
#         prev.next = nxt.prev = node
#         node.next, node.prev = nxt, prev

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].val
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key])

#         if len(self.cache) > self.cap:
#             # remove from the list and delete the LRU from hashmap
#             lru = self.left.next
#             self.remove(lru)
#             del self.cache[lru.key]

# DSA Approach (Concise Prep Checklist)
# 1. Repeat the question
# - Restate problem in one sentence (inputs -> transformation -> output)
# - Confirm input types, indexing (0 vs 1), single vs multiple test cases
# - Ask edge cases: empty, single element, duplicates, negatives, overflow
# - Confirm allowed operations: modify input, sort, extra memory, recursion limits
# - Clarify constraints: max/min n, value ranges, time/memory limits, target Big-O
# - Confirm output format, ordering, stability, tie-breakers, no-solution behavior
# - Ask for 1 normal + 1 tricky example with expected output
# - Confirm environment expectations: libraries, full I/O vs function only, tests required

# 2. Clarifying questions
# - Inputs: type, size, range, sorted?, mutable?
# - Outputs: format, order, duplicates allowed?
# - Constraints: n, value bounds, performance target
# - Sorting: allowed? stability required?
# - Memory: fits in memory or streaming?
# - Special cases: empty, all same, extreme values, cycles (if applicable)

# 3. Work through an example
# - Use small sample input
# - Step through logic manually
# - Track pointers/stack/queue/map state
# - Verify expected output and edge behavior

# 4. Brainstorm solutions
# - Identify pattern: hash, two pointers, sliding window, stack, heap, BFS/DFS, DP, greedy
# - Start with brute force and its Big-O
# - Propose optimal approach and tradeoffs
# - Match data structure to need (lookup, ordering, top-k, dependencies)

# 5. Step out the solution
# - Choose approach + data structures
# - Write steps in plain logic/pseudocode
# - Define loop invariants
# - Dry-run on example
# - State time and space complexity

# 6. Convert to code
# - Translate steps directly to code
# - Comment intent and invariants
# - Handle edge cases early
# - Re-run example and edge cases mentally
# 7. Verify and explain
# - Restate final Big-O
# - Explain correctness briefly
# - Mention alternative approaches if asked

