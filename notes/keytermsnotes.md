## Keyword → Algorithm Cheat Sheet

Use this guide to quickly map common problem phrasing (“keywords”) to a likely pattern.

---

## Top K

- **Heap / Priority Queue**
	- [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

---

## “How many ways…?” (Counting)

- **DFS / Backtracking** or **DP (counting)**
	- [Decode Ways](https://leetcode.com/problems/decode-ways/)
	- [Unique Paths](https://leetcode.com/problems/unique-paths/)

---

## Substring

- **Sliding Window**
	- [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## Palindrome

- **Two Pointers**
	- [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- **DFS / Backtracking**
	- [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
- **DP**
	- [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/)

---

## Tree

- If you see **shortest** / **level-order** / “by level” → **BFS**
	- [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- Otherwise, many “compute depth / path / recursion” tasks → **DFS**
	- [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

---

## Parentheses

- **Stack**
	- [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

---

## Subarray

- **Sliding Window** (often fixed window)
	- [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)
- **Prefix Sum** (counting/range sums)
	- [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
- **Prefix Sum + Hash Map** (mod / repeated sum patterns)
	- [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

---

## Max Subarray

- **Greedy (Kadane’s Algorithm)**
	- [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

---

## “X Sum” / Pair Sum

- **Hash Map** or **Two Pointers** (depending on sorted vs unsorted)
	- [Two Sum](https://leetcode.com/problems/two-sum/)

---

## Max / Longest Sequence

- **DP (LIS-style)** / **DFS + memo**
	- [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- **Monotonic Deque** (max over sliding window)
	- [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

---

## Minimum / Shortest

- **DP** (grid/path minimization)
	- [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
- **BFS** (shortest path in unweighted graph)
	- [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

---

## Partition / Split Array or String

- **DFS / Backtracking** (enumerate splits)
	- [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
- **DP** (count/minimize over splits)
	- [Decode Ways](https://leetcode.com/problems/decode-ways/)

---

## Subsequence

- **DP / DFS + memo**
	- [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
	- [Is Subsequence](https://leetcode.com/problems/is-subsequence/)

---

## Matrix

- **BFS / DFS** (flood fill / islands / connected components)
	- [Flood Fill](https://leetcode.com/problems/flood-fill/)
	- [Number of Islands](https://leetcode.com/problems/number-of-islands/)
- **DP**
	- [Maximal Square](https://leetcode.com/problems/maximal-square/)

---

## Jump

- **Greedy / DP**
	- [Jump Game](https://leetcode.com/problems/jump-game/)

---

## Game

- **DP (game DP)**
	- [Divisor Game](https://leetcode.com/problems/divisor-game/)
	- [Stone Game](https://leetcode.com/problems/stone-game/)

---

## Connected Components / Regions / Groups

- **Union Find** or **BFS/DFS**
	- [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
	- [Redundant Connection](https://leetcode.com/problems/redundant-connection/)

---

## Transitive Relationships

If relationships are **transitive** (A~B and B~C implies A~C), model it as a **graph** and use **BFS/DFS**, or use **Union Find**.

- **String converting to another** → **BFS**
	- [Word Ladder](https://leetcode.com/problems/word-ladder/)
- **String similarity / equivalence** → **BFS/DFS** or **Union Find**
	- [Sentence Similarity II](https://leetcode.com/problems/sentence-similarity-ii/)
- **Division / ratio relationships** → **Graph + BFS/DFS** (or Union Find)
	- [Evaluate Division](https://leetcode.com/problems/evaluate-division/)

---

## Interval

- **Greedy** (sort by start/end, then sweep/merge)
	- [Merge Intervals](https://leetcode.com/problems/merge-intervals/)


