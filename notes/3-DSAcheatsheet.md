Perfect — below is an **expanded, interview-grade DSA data-structures cheat sheet** with **more theory, concrete LeetCode examples, and usage mechanics**, while staying **dense, scannable, and zero-fluff**. This is calibrated for **Meta / Google / Amazon / Atlassian** expectations.

---

# ARRAYS / DYNAMIC ARRAYS

**Intuition:** Contiguous memory, constant-time indexed access

**Core ops & complexity**

* Access: O(1)
* Append: O(1) amortized
* Insert/Delete (middle): O(n)
* Space: O(n)

**Optimal for**

* Ordered data
* Fast iteration and random access
* Cache-friendly scans

**Common patterns**

* Two pointers
* Sliding window
* Prefix sums
* Sorting + scanning

**Theory / how to use**

* Convert brute force O(n²) → O(n) using sliding window
* Precompute prefix sums to answer range queries in O(1)
* Combine with sorting to enable two pointers or binary search

**Example LeetCode problems**

* Two Sum (after sorting variant)
* Best Time to Buy and Sell Stock
* Container With Most Water
* Subarray Sum Equals K (with prefix sum + hashmap)

**Trade-offs / pitfalls**

* Middle insertions are expensive
* Watch off-by-one errors
* Resizing cost is amortized, not guaranteed

**Use this when**

* Order matters
* You need fast index access
* You’re scanning left → right once

---

# STRINGS

**Intuition:** Immutable array of characters

**Core ops & complexity**

* Access: O(1)
* Substring: O(n)
* Concatenation: O(n)
* Space: O(n)

**Optimal for**

* Character-based logic
* Pattern matching

**Common patterns**

* Sliding window
* Two pointers
* Frequency arrays
* Rolling hash

**Theory / how to use**

* Treat as array of chars
* Use frequency maps instead of modifying strings
* Prefer indices over slicing

**Example LeetCode problems**

* Longest Substring Without Repeating Characters
* Valid Anagram
* Minimum Window Substring
* Palindromic Substrings

**Trade-offs / pitfalls**

* Immutability causes hidden copies
* Unicode assumptions can break solutions

**Use this when**

* Problem explicitly references characters or substrings

---

# HASH MAP (DICTIONARY)

**Intuition:** O(1) average lookup by key

**Core ops & complexity**

* Insert / Lookup / Delete: O(1) average
* Space: O(n)

**Optimal for**

* Fast lookup
* Counting
* Caching

**Common patterns**

* Frequency counting
* Index mapping
* Prefix sum lookup
* Memoization (DP)

**Theory / how to use**

* Trade space for time
* Store “state so far” while iterating
* Combine with prefix sums to avoid nested loops

**Example LeetCode problems**

* Two Sum
* Subarray Sum Equals K
* Group Anagrams
* Longest Consecutive Sequence

**Trade-offs / pitfalls**

* Hash collisions (rare but theoretical)
* Memory heavy
* Order not guaranteed (unless ordered map)

**Use this when**

* You need instant access by value
* Replacing O(n) search with O(1)

---

# HASH SET

**Intuition:** Fast membership checking

**Core ops & complexity**

* Add / Remove / Contains: O(1) average
* Space: O(n)

**Optimal for**

* Deduplication
* Visited tracking

**Common patterns**

* Cycle detection
* Unique elements
* Seen-before checks

**Theory / how to use**

* Use to short-circuit repeated work
* Often paired with DFS/BFS

**Example LeetCode problems**

* Contains Duplicate
* Longest Consecutive Sequence
* Happy Number

**Trade-offs / pitfalls**

* No ordering
* Cannot count frequencies

**Use this when**

* You only care if something exists

---

# STACK

**Intuition:** Last-In-First-Out

**Core ops & complexity**

* Push / Pop / Peek: O(1)
* Space: O(n)

**Optimal for**

* Reversal
* Backtracking
* State tracking

**Common patterns**

* Monotonic stack
* Parentheses validation
* DFS

**Theory / how to use**

* Use monotonic stacks to find next greater/smaller elements
* Stack represents “unfinished work”

**Example LeetCode problems**

* Valid Parentheses
* Daily Temperatures
* Next Greater Element
* Evaluate Reverse Polish Notation

**Trade-offs / pitfalls**

* Forgetting stack invariant
* Recursive stack overflow

**Use this when**

* You need to process elements in reverse dependency order

---

# QUEUE

**Intuition:** First-In-First-Out

**Core ops & complexity**

* Enqueue / Dequeue: O(1)
* Space: O(n)

**Optimal for**

* Level-order processing

**Common patterns**

* BFS
* Scheduling
* Layered traversal

**Theory / how to use**

* BFS guarantees shortest path in unweighted graphs
* Process data in “waves”

**Example LeetCode problems**

* Binary Tree Level Order Traversal
* Rotting Oranges
* Number of Islands (BFS)

**Trade-offs / pitfalls**

* Using array instead of deque leads to O(n) pops

**Use this when**

* Order of processing matters across levels

---

# DEQUE

**Intuition:** Queue with both ends

**Core ops & complexity**

* All operations: O(1)

**Optimal for**

* Sliding window min/max

**Common patterns**

* Monotonic queue

**Theory / how to use**

* Maintain decreasing/increasing order
* Pop obsolete elements when window slides

**Example LeetCode problems**

* Sliding Window Maximum
* Shortest Subarray with Sum ≥ K

**Trade-offs / pitfalls**

* Logic complexity
* Must maintain strict invariants

**Use this when**

* You need window extrema in O(1)

---

# LINKED LIST

**Intuition:** Nodes connected by pointers

**Core ops & complexity**

* Insert/Delete (given node): O(1)
* Search: O(n)

**Optimal for**

* Frequent structural changes

**Common patterns**

* Pointer manipulation
* Cycle detection
* Reversal

**Theory / how to use**

* Use slow/fast pointers
* Reverse via iterative pointer rewiring

**Example LeetCode problems**

* Reverse Linked List
* Linked List Cycle
* Merge Two Sorted Lists

**Trade-offs / pitfalls**

* Pointer bugs
* No random access

**Use this when**

* Interview explicitly wants it
* Structure changes often

---

# HEAP (PRIORITY QUEUE)

**Intuition:** Efficiently access min or max

**Core ops & complexity**

* Push / Pop: O(log n)
* Peek: O(1)

**Optimal for**

* Top-K problems
* Greedy selection

**Common patterns**

* K largest/smallest
* Scheduling
* Merging sorted data

**Theory / how to use**

* Keep heap size fixed for top-K
* Use min-heap to track largest elements

**Example LeetCode problems**

* Kth Largest Element
* Top K Frequent Elements
* Merge K Sorted Lists

**Trade-offs / pitfalls**

* Not good for arbitrary deletion
* Heap logic must be precise

**Use this when**

* You repeatedly need best candidate so far

---

# TREE (GENERAL / BINARY)

**Intuition:** Hierarchical structure

**Core ops & complexity**

* Traversal: O(n)
* Space: O(n)

**Optimal for**

* Hierarchical data
* Recursive logic

**Common patterns**

* DFS / BFS
* Recursion
* Path aggregation

**Theory / how to use**

* DFS for path-based problems
* BFS for level-based problems

**Example LeetCode problems**

* Maximum Depth of Binary Tree
* Path Sum
* Lowest Common Ancestor

**Trade-offs / pitfalls**

* Stack overflow
* Forgetting base cases

**Use this when**

* Problem describes parent/child relationships

---

# GRAPH

**Intuition:** Nodes + edges

**Core ops & complexity**

* Traversal: O(V + E)

**Optimal for**

* Relationship problems
* Network modeling

**Common patterns**

* BFS / DFS
* Topological sort
* Shortest path

**Theory / how to use**

* Use adjacency list
* Track visited to avoid cycles

**Example LeetCode problems**

* Course Schedule
* Number of Islands
* Clone Graph

**Trade-offs / pitfalls**

* Directed vs undirected confusion
* Forgetting visited set

**Use this when**

* Data is non-linear and interconnected

---

# UNION FIND (DISJOINT SET)

**Intuition:** Tracks connected components

**Core ops & complexity**

* Union / Find: ~O(1) amortized

**Optimal for**

* Connectivity queries

**Common patterns**

* Dynamic graph connectivity
* MST

**Theory / how to use**

* Path compression
* Union by rank

**Example LeetCode problems**

* Number of Connected Components
* Accounts Merge

**Trade-offs / pitfalls**

* Hard to derive from scratch

**Use this when**

* Repeated “are these connected?” queries

---

# SEGMENT TREE / BIT

**Intuition:** Efficient range queries

**Core ops & complexity**

* Query / Update: O(log n)

**Optimal for**

* Dynamic range queries

**Common patterns**

* Range sum/min/max

**Theory / how to use**

* Segment tree for complex ranges
* BIT for prefix sums

**Example LeetCode problems**

* Range Sum Query Mutable
* Count of Smaller Numbers After Self

**Trade-offs / pitfalls**

* Implementation complexity

**Use this when**

* Range queries + updates are frequent

---

# FINAL INTERVIEW DECISION RULES

* **Need lookup →** HashMap / Set
* **Need order →** Heap / BST
* **Need window extrema →** Deque
* **Need connectivity →** Union Find
* **Need hierarchy →** Tree
* **Need relationships →** Graph

---

If you want next, I can:

* Compress this into a **1-page Python comment**
* Turn it into a **decision tree flowchart**
* Map directly to **NeetCode 150 / Meta tags**
* Add **interviewer justification scripts (“why this DS”)**

Just tell me the format.
