# DSA Interview Study Guide — Source of Truth

> Python-first. Templates you can adapt in-place for any problem.

---

## Table of Contents

1. [Decision Framework — Which Pattern?](#1-decision-framework--which-pattern)
2. [Arrays & Hashing](#2-arrays--hashing)
3. [Two Pointers](#3-two-pointers)
4. [Sliding Window](#4-sliding-window)
5. [Prefix Sums](#5-prefix-sums)
6. [Binary Search](#6-binary-search)
7. [Linked Lists](#7-linked-lists)
8. [Stacks & Monotonic Stack](#8-stacks--monotonic-stack)
9. [Trees — DFS & BFS](#9-trees--dfs--bfs)
10. [Graphs — DFS, BFS, Topological Sort](#10-graphs--dfs-bfs-topological-sort)
11. [Heaps / Priority Queue](#11-heaps--priority-queue)
12. [Backtracking — Subsets, Permutations, Combinations](#12-backtracking--subsets-permutations-combinations)
13. [Dynamic Programming](#13-dynamic-programming)
14. [Intervals](#14-intervals)
15. [Greedy](#15-greedy)
16. [Tries](#16-tries)
17. [Union-Find (Disjoint Set)](#17-union-find-disjoint-set)
18. [Bit Manipulation](#18-bit-manipulation)
19. [Complexity Cheat Sheet](#19-complexity-cheat-sheet)

---

## 1. Decision Framework — Which Pattern?

```
Input is a sorted array / rotated sorted?  → Binary Search
Contiguous subarray / substring?           → Sliding Window or Prefix Sum
Pair / triplet in array?                   → Two Pointers (sorted) or HashMap
All subsets / combinations / permutations? → Backtracking
Shortest path (unweighted)?                → BFS
Shortest path (weighted)?                  → Dijkstra (heapq)
Connected components / cycle detection?    → DFS or Union-Find
Ordering with dependencies?                → Topological Sort
Overlapping subproblems, optimal substructure? → DP
Top-K / K-th largest?                      → Heap
Nested structure / valid brackets?         → Stack
Prefix matching / autocomplete?            → Trie
```

---

## 2. Arrays & Hashing

### Key ideas
- `Counter` / `defaultdict` for frequency maps
- Sorting to group anagrams, detect duplicates
- HashMap for O(1) lookup (Two-Sum style)

```python
from collections import Counter, defaultdict

# ── Two-Sum ──────────────────────────────────────────────
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}                          # val → index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i
    return []

# ── Group Anagrams ───────────────────────────────────────
def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[tuple, list[str]] = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))        # or tuple(Counter(s))
        groups[key].append(s)
    return list(groups.values())

# ── Contains Duplicate within k distance ─────────────────
def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    last_seen: dict[int, int] = {}
    for i, n in enumerate(nums):
        if n in last_seen and i - last_seen[n] <= k:
            return True
        last_seen[n] = i
    return False
```

**Signals**: "find pair", "count occurrences", "group by some key"

---

## 3. Two Pointers

### Key ideas
- Array must be **sorted** (or you sort it first)
- `left` and `right` collapse inward; or both move right (fast/slow)
- Avoids O(n²) nested loops

```python
# ── Two-Sum (sorted array) ───────────────────────────────
def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l, r]
        elif s < target:
            l += 1
        else:
            r -= 1
    return []

# ── 3-Sum ────────────────────────────────────────────────
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:   # skip duplicates
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]: l += 1
                while l < r and nums[r] == nums[r-1]: r -= 1
                l += 1; r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res

# ── Fast / Slow (cycle detection in linked list) ─────────
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

**Signals**: sorted array, "pairs that sum to", container with most water, valid palindrome

---

## 4. Sliding Window

### Two flavors
| Type | When | Shrink condition |
|------|------|-----------------|
| Fixed size | window size given | always remove `nums[i - k]` |
| Variable size | max/min length with constraint | shrink while constraint violated |

```python
# ── Fixed window: max sum of size k ──────────────────────
def max_sum_window(nums: list[int], k: int) -> int:
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        best = max(best, window_sum)
    return best

# ── Variable window: longest substring without repeating ─
def length_of_longest_substring(s: str) -> int:
    char_set: set[str] = set()
    l = 0
    best = 0
    for r, c in enumerate(s):
        while c in char_set:         # shrink until valid
            char_set.remove(s[l])
            l += 1
        char_set.add(c)
        best = max(best, r - l + 1)
    return best

# ── Variable window: minimum window substring ────────────
from collections import Counter

def min_window(s: str, t: str) -> str:
    need = Counter(t)
    have, required = 0, len(need)
    freq: dict[str, int] = {}
    l, best_l, best_r = 0, -1, len(s)   # sentinels

    for r, c in enumerate(s):
        freq[c] = freq.get(c, 0) + 1
        if c in need and freq[c] == need[c]:
            have += 1
        while have == required:
            if r - l < best_r - best_l:
                best_l, best_r = l, r
            freq[s[l]] -= 1
            if s[l] in need and freq[s[l]] < need[s[l]]:
                have -= 1
            l += 1

    return "" if best_l == -1 else s[best_l:best_r + 1]
```

**Signals**: "subarray/substring", "longest/shortest with property", "at most k distinct"

---

## 5. Prefix Sums

### Key ideas
- `prefix[i]` = sum of `nums[0..i-1]` (with leading 0)
- Range sum `[i, j]` = `prefix[j+1] - prefix[i]`
- Combine with HashMap for "subarray sum = k"

```python
# ── Build prefix array ───────────────────────────────────
def build_prefix(nums: list[int]) -> list[int]:
    ps = [0]
    for x in nums:
        ps.append(ps[-1] + x)
    return ps                         # len = n+1

def range_sum(ps: list[int], i: int, j: int) -> int:
    return ps[j + 1] - ps[i]         # sum nums[i..j] inclusive

# ── Subarray sum equals k (count) ────────────────────────
def subarray_sum(nums: list[int], k: int) -> int:
    count = 0
    prefix = 0
    seen = {0: 1}                     # prefix_sum → how many times seen
    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count

# ── 2-D prefix sum ───────────────────────────────────────
def build_2d_prefix(matrix: list[list[int]]) -> list[list[int]]:
    m, n = len(matrix), len(matrix[0])
    ps = [[0] * (n + 1) for _ in range(m + 1)]
    for r in range(1, m + 1):
        for c in range(1, n + 1):
            ps[r][c] = (matrix[r-1][c-1]
                        + ps[r-1][c] + ps[r][c-1] - ps[r-1][c-1])
    return ps

def region_sum(ps, r1, c1, r2, c2):   # inclusive, 0-indexed
    return (ps[r2+1][c2+1] - ps[r1][c2+1]
            - ps[r2+1][c1] + ps[r1][c1])
```

**Signals**: range queries, "sum of subarray", immutable array with repeated queries

---

## 6. Binary Search

### Key idea: always think about what condition the left/right halves satisfy

```python
# ── Classic: exact target ────────────────────────────────
def binary_search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# ── Left boundary (first index where nums[i] >= target) ──
def lower_bound(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)              # r = len (exclusive)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l                         # insertion point

# ── Search on answer space ───────────────────────────────
def min_days_to_make_bouquets(bloomDay, m, k):
    """Binary search on the answer (number of days)."""
    def can_make(days: int) -> bool:
        bouquets = flowers = 0
        for d in bloomDay:
            if d <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m

    l, r = min(bloomDay), max(bloomDay)
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if can_make(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

# ── Rotated sorted array ─────────────────────────────────
def search_rotated(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:           # left half is sorted
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:                              # right half is sorted
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
```

**Signals**: sorted input, "minimum/maximum feasible value", "first/last occurrence"

---

## 7. Linked Lists

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ── Reverse in-place ─────────────────────────────────────
def reverse(head: ListNode) -> ListNode:
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# ── Find middle (slow/fast) ──────────────────────────────
def middle(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow                        # for even len → second middle

# ── Merge two sorted lists ───────────────────────────────
def merge(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1; l1 = l1.next
        else:
            curr.next = l2; l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next

# ── Remove n-th from end ─────────────────────────────────
def remove_nth(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):            # advance fast n+1 steps
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next        # remove node
    return dummy.next
```

**Signals**: in-place operation, cycle, "k from end", merge, palindrome check

---

## 8. Stacks & Monotonic Stack

```python
# ── Valid Parentheses ────────────────────────────────────
def is_valid(s: str) -> bool:
    stack = []
    close = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in close:
            if not stack or stack[-1] != close[c]:
                return False
            stack.pop()
        else:
            stack.append(c)
    return not stack

# ── Monotonic stack: next greater element ────────────────
def next_greater(nums: list[int]) -> list[int]:
    res = [-1] * len(nums)
    stack = []                         # indices, decreasing values
    for i, n in enumerate(nums):
        while stack and nums[stack[-1]] < n:
            res[stack.pop()] = n
        stack.append(i)
    return res

# ── Largest rectangle in histogram ───────────────────────
def largest_rectangle(heights: list[int]) -> int:
    stack = []                         # (index, height) monotonic inc
    max_area = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, ht = stack.pop()
            max_area = max(max_area, ht * (i - idx))
            start = idx
        stack.append((start, h))
    for idx, ht in stack:
        max_area = max(max_area, ht * (len(heights) - idx))
    return max_area

# ── Min stack ────────────────────────────────────────────
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []            # tracks current min

    def push(self, val: int) -> None:
        self.stack.append(val)
        m = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(m)

    def pop(self) -> None:
        self.stack.pop(); self.min_stack.pop()

    def top(self) -> int: return self.stack[-1]
    def get_min(self) -> int: return self.min_stack[-1]
```

**Signals**: nested, matching brackets, "next greater/smaller", temperatures, histogram

---

## 9. Trees — DFS & BFS

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

# ── DFS traversals (recursive) ───────────────────────────
def inorder(root):    # left → root → right  (sorted for BST)
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

def preorder(root):   # root → left → right
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

def postorder(root):  # left → right → root
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []

# ── Height / max depth ───────────────────────────────────
def max_depth(root) -> int:
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# ── BFS / level-order ────────────────────────────────────
from collections import deque

def level_order(root) -> list[list[int]]:
    if not root: return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):        # process one level at a time
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res

# ── Lowest Common Ancestor ───────────────────────────────
def lca(root, p, q):
    if not root or root is p or root is q:
        return root
    left  = lca(root.left,  p, q)
    right = lca(root.right, p, q)
    return root if left and right else left or right

# ── Validate BST ─────────────────────────────────────────
def is_valid_bst(root, lo=float('-inf'), hi=float('inf')) -> bool:
    if not root: return True
    if not (lo < root.val < hi): return False
    return (is_valid_bst(root.left,  lo, root.val) and
            is_valid_bst(root.right, root.val, hi))

# ── DFS iterative (pre-order) ────────────────────────────
def dfs_iter(root):
    if not root: return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right: stack.append(node.right)   # right first
        if node.left:  stack.append(node.left)
    return res
```

**Signals**: tree height, path sum, serialize/deserialize, kth smallest (BST inorder), LCA

---

## 10. Graphs — DFS, BFS, Topological Sort

```python
from collections import deque, defaultdict

# ── Build adjacency list ─────────────────────────────────
def build_graph(n: int, edges: list[list[int]], directed=False) -> dict:
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        if not directed: g[v].append(u)
    return g

# ── DFS (recursive) ─────────────────────────────────────
def dfs(graph, node, visited=None):
    if visited is None: visited = set()
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# ── BFS: shortest path (unweighted) ─────────────────────
def bfs_shortest(graph, start, end):
    dist = {start: 0}
    q = deque([start])
    while q:
        node = q.popleft()
        if node == end: return dist[end]
        for nb in graph[node]:
            if nb not in dist:
                dist[nb] = dist[node] + 1
                q.append(nb)
    return -1

# ── Grid BFS (4-directional) ─────────────────────────────
def bfs_grid(grid, sr, sc):
    ROWS, COLS = len(grid), len(grid[0])
    visited = {(sr, sc)}
    q = deque([(sr, sc, 0)])           # (row, col, steps)
    while q:
        r, c, steps = q.popleft()
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < ROWS and 0 <= nc < COLS
                    and (nr, nc) not in visited
                    and grid[nr][nc] != '#'):
                visited.add((nr, nc))
                q.append((nr, nc, steps + 1))

# ── DFS on grid (flood fill / islands) ──────────────────
def num_islands(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or r >= ROWS or c < 0 or c >= COLS
                or (r, c) in visited or grid[r][c] == '0'):
            return
        visited.add((r, c))
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            dfs(r + dr, c + dc)

    count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                count += 1
    return count

# ── Topological Sort (Kahn's BFS) ────────────────────────
def topo_sort(n: int, prereqs: list[list[int]]) -> list[int]:
    graph = defaultdict(list)
    indegree = [0] * n
    for a, b in prereqs:               # b → a (b is prereq of a)
        graph[b].append(a)
        indegree[a] += 1

    q = deque([i for i in range(n) if indegree[i] == 0])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nb in graph[node]:
            indegree[nb] -= 1
            if indegree[nb] == 0:
                q.append(nb)
    return order if len(order) == n else []   # [] = cycle

# ── Dijkstra (weighted shortest path) ───────────────────
import heapq

def dijkstra(n: int, graph: dict, src: int) -> list[int]:
    dist = [float('inf')] * n
    dist[src] = 0
    heap = [(0, src)]                  # (distance, node)
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue       # stale entry
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist
```

**Signals**: connected components, cycle detection, shortest path, course schedule, clone graph

---

## 11. Heaps / Priority Queue

```python
import heapq

# Python heapq is a MIN-heap by default.
# For MAX-heap: negate values  →  heappush(h, -val)

# ── Kth largest element ───────────────────────────────────
def kth_largest(nums: list[int], k: int) -> int:
    # keep a min-heap of size k
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

# ── Merge k sorted lists ──────────────────────────────────
def merge_k_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    dummy = curr = ListNode()
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next

# ── Task scheduler ───────────────────────────────────────
from collections import Counter

def least_interval(tasks: list[str], n: int) -> int:
    freq = Counter(tasks)
    max_heap = [-cnt for cnt in freq.values()]
    heapq.heapify(max_heap)
    time = 0
    queue = deque()                    # (count, available_at)
    while max_heap or queue:
        time += 1
        if max_heap:
            cnt = 1 + heapq.heappop(max_heap)  # decrement (negated)
            if cnt:
                queue.append((cnt, time + n))
        if queue and queue[0][1] == time:
            heapq.heappush(max_heap, queue.popleft()[0])
    return time

# ── Two heaps: median of data stream ─────────────────────
class MedianFinder:
    def __init__(self):
        self.low  = []    # max-heap (negated)
        self.high = []    # min-heap

    def add_num(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        if self.low and self.high and (-self.low[0]) > self.high[0]:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self) -> float:
        if len(self.low) > len(self.high): return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2
```

**Signals**: "top K", "K closest", "median", "schedule tasks", merge sorted

---

## 12. Backtracking — Subsets, Permutations, Combinations

> **Template**: choose → recurse → unchoose

```python
# ── Subsets (no duplicates) ──────────────────────────────
def subsets(nums: list[int]) -> list[list[int]]:
    res = []
    def backtrack(start: int, path: list[int]):
        res.append(path[:])            # snapshot at every node
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return res

# ── Subsets II (with duplicates) ─────────────────────────
def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    def backtrack(start: int, path: list[int]):
        res.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:   # skip dup
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return res

# ── Permutations (no duplicates) ─────────────────────────
def permutations(nums: list[int]) -> list[list[int]]:
    res = []
    def backtrack(path: list[int], used: set):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i, n in enumerate(nums):
            if i in used: continue
            used.add(i)
            path.append(n)
            backtrack(path, used)
            path.pop()
            used.remove(i)
    backtrack([], set())
    return res

# ── Combinations: choose k from 1..n ─────────────────────
def combinations(n: int, k: int) -> list[list[int]]:
    res = []
    def backtrack(start: int, path: list[int]):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    backtrack(1, [])
    return res

# ── Combination Sum (reuse elements) ─────────────────────
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    candidates.sort()
    def backtrack(start: int, path: list[int], remaining: int):
        if remaining == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining: break   # pruning
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])  # i not i+1: reuse
            path.pop()
    backtrack(0, [], target)
    return res

# ── Word Search (backtracking on grid) ───────────────────
def word_search(board: list[list[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])

    def dfs(r, c, idx):
        if idx == len(word): return True
        if (r < 0 or r >= ROWS or c < 0 or c >= COLS
                or board[r][c] != word[idx]): return False
        tmp, board[r][c] = board[r][c], '#'      # mark visited
        found = any(dfs(r+dr, c+dc, idx+1) for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)])
        board[r][c] = tmp                         # restore
        return found

    return any(dfs(r, c, 0) for r in range(ROWS) for c in range(COLS))
```

**Decision tree**:
- Subsets → collect at every node, `start` moves right
- Permutations → collect at leaf, use a `used` set
- Combinations → collect at leaf, `start` moves right, fixed size k
- Combination Sum → collect at leaf, reuse by not advancing `start`

---

## 13. Dynamic Programming

### Framework
1. Define what `dp[i]` (or `dp[i][j]`) represents
2. Write the recurrence
3. Identify base cases
4. Choose: top-down (memoization) or bottom-up (tabulation)

```python
# ── Memoization template ─────────────────────────────────
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(state):
    # base case
    if ...: return ...
    # recurrence
    return min/max(dp(next_state1), dp(next_state2), ...)

# ── Fibonacci (bottom-up, O(1) space) ────────────────────
def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a

# ── Climbing Stairs / Coin Change (1-D DP) ───────────────
def climb_stairs(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def coin_change(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a-c] + 1)
    return -1 if dp[amount] == float('inf') else dp[amount]

# ── Longest Increasing Subsequence ───────────────────────
def lis(nums: list[int]) -> int:
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# O(n log n) version using patience sorting:
import bisect
def lis_fast(nums: list[int]) -> int:
    tails = []
    for n in nums:
        pos = bisect.bisect_left(tails, n)
        if pos == len(tails): tails.append(n)
        else: tails[pos] = n
    return len(tails)

# ── 0/1 Knapsack ─────────────────────────────────────────
def knapsack(capacity: int, weights: list[int], values: list[int]) -> int:
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for cap in range(capacity, w - 1, -1):   # reverse to avoid reuse
            dp[cap] = max(dp[cap], dp[cap - w] + v)
    return dp[capacity]

# ── Longest Common Subsequence (2-D DP) ──────────────────
def lcs(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# ── Edit Distance ─────────────────────────────────────────
def edit_distance(w1: str, w2: str) -> int:
    m, n = len(w1), len(w2)
    dp = list(range(n + 1))
    for i in range(1, m + 1):
        prev = dp[:]
        dp[0] = i
        for j in range(1, n + 1):
            if w1[i-1] == w2[j-1]:
                dp[j] = prev[j-1]
            else:
                dp[j] = 1 + min(prev[j], dp[j-1], prev[j-1])
    return dp[n]

# ── House Robber ─────────────────────────────────────────
def rob(nums: list[int]) -> int:
    prev2 = prev1 = 0
    for n in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + n)
    return prev1
```

### Common DP Patterns

| Problem type | State | Recurrence |
|---|---|---|
| 1-D linear | `dp[i]` | depends on `dp[i-1]`, `dp[i-2]` |
| 2-D grid | `dp[r][c]` | from top/left neighbors |
| Subsequence | `dp[i][j]` on two strings | match or skip |
| Knapsack | `dp[capacity]` | take or skip item |
| Interval DP | `dp[l][r]` | split at every k in [l,r] |

---

## 14. Intervals

```python
# ── Merge overlapping intervals ───────────────────────────
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()                   # sort by start
    res = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= res[-1][1]:        # overlaps
            res[-1][1] = max(res[-1][1], end)
        else:
            res.append([start, end])
    return res

# ── Insert interval ───────────────────────────────────────
def insert_interval(intervals: list[list[int]], new: list[int]) -> list[list[int]]:
    res = []
    i = 0
    # add all before new
    while i < len(intervals) and intervals[i][1] < new[0]:
        res.append(intervals[i]); i += 1
    # merge overlapping
    while i < len(intervals) and intervals[i][0] <= new[1]:
        new[0] = min(new[0], intervals[i][0])
        new[1] = max(new[1], intervals[i][1])
        i += 1
    res.append(new)
    # add remaining
    while i < len(intervals):
        res.append(intervals[i]); i += 1
    return res

# ── Meeting rooms II (min rooms needed) ──────────────────
def min_meeting_rooms(intervals: list[list[int]]) -> int:
    starts = sorted(s for s, e in intervals)
    ends   = sorted(e for s, e in intervals)
    rooms = count = 0
    j = 0
    for s in starts:
        if s < ends[j]:
            count += 1
        else:
            j += 1
        rooms = max(rooms, count)
    return rooms
```

---

## 15. Greedy

> Greedy works when a locally optimal choice leads to a globally optimal solution. Prove by exchange argument.

```python
# ── Jump Game ─────────────────────────────────────────────
def can_jump(nums: list[int]) -> bool:
    reach = 0
    for i, n in enumerate(nums):
        if i > reach: return False
        reach = max(reach, i + n)
    return True

# ── Jump Game II (min jumps) ──────────────────────────────
def jump(nums: list[int]) -> int:
    jumps = curr_end = furthest = 0
    for i in range(len(nums) - 1):
        furthest = max(furthest, i + nums[i])
        if i == curr_end:
            jumps += 1
            curr_end = furthest
    return jumps

# ── Gas Station ───────────────────────────────────────────
def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost): return -1
    tank = start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start

# ── Activity selection / non-overlapping intervals ────────
def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])   # sort by end time
    count = 0
    last_end = float('-inf')
    for start, end in intervals:
        if start >= last_end:
            last_end = end
        else:
            count += 1                    # remove this interval
    return count
```

---

## 16. Tries

```python
class TrieNode:
    def __init__(self):
        self.children: dict[str, 'TrieNode'] = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children: return False
            node = node.children[c]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children: return False
            node = node.children[c]
        return True

    def search_with_wildcard(self, word: str) -> bool:
        """'.' matches any single character."""
        def dfs(node: TrieNode, i: int) -> bool:
            if i == len(word): return node.is_end
            c = word[i]
            if c == '.':
                return any(dfs(child, i+1) for child in node.children.values())
            if c not in node.children: return False
            return dfs(node.children[c], i+1)
        return dfs(self.root, 0)
```

**Signals**: prefix search, autocomplete, word dictionary with wildcards

---

## 17. Union-Find (Disjoint Set)

```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank   = [0] * n
        self.count  = n                # number of components

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py: return False      # already connected
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]: self.rank[px] += 1
        self.count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

# ── Usage: number of islands ─────────────────────────────
def num_islands_uf(grid):
    ROWS, COLS = len(grid), len(grid[0])
    uf = UnionFind(ROWS * COLS)
    count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '1':
                count += 1
                for dr, dc in [(0,1),(1,0)]:
                    nr, nc = r+dr, c+dc
                    if nr < ROWS and nc < COLS and grid[nr][nc] == '1':
                        if uf.union(r*COLS+c, nr*COLS+nc):
                            count -= 1
    return count
```

**Signals**: connected components, cycle in undirected graph, redundant connection, accounts merge

---

## 18. Bit Manipulation

```python
# Common tricks
x & (x - 1)       # clear lowest set bit  (Brian Kernighan)
x & (-x)          # isolate lowest set bit
x ^ x == 0        # x XOR itself = 0
n & 1             # check if odd
n >> 1            # divide by 2
n << 1            # multiply by 2

# ── Count set bits ────────────────────────────────────────
def hamming_weight(n: int) -> int:
    count = 0
    while n:
        n &= n - 1    # clear lowest bit
        count += 1
    return count

# ── Missing number (XOR) ──────────────────────────────────
def missing_number(nums: list[int]) -> int:
    xor = len(nums)
    for i, n in enumerate(nums):
        xor ^= i ^ n
    return xor

# ── Single number (every element appears twice except one) ─
def single_number(nums: list[int]) -> int:
    res = 0
    for n in nums: res ^= n
    return res

# ── Power of two ─────────────────────────────────────────
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

# ── Generate all subsets via bitmask ─────────────────────
def subsets_bitmask(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    result = []
    for mask in range(1 << n):                 # 0 to 2^n - 1
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        result.append(subset)
    return result
```

---

## 19. Complexity Cheat Sheet

| Pattern | Time | Space |
|---|---|---|
| HashMap lookup | O(1) | O(n) |
| Sorting | O(n log n) | O(1)–O(n) |
| Binary search | O(log n) | O(1) |
| Sliding window | O(n) | O(1)–O(k) |
| Prefix sum build | O(n) | O(n) |
| BFS/DFS graph | O(V + E) | O(V) |
| BFS/DFS grid | O(m × n) | O(m × n) |
| Dijkstra | O((V+E) log V) | O(V) |
| Backtracking subsets | O(2^n · n) | O(n) |
| Backtracking perms | O(n! · n) | O(n) |
| DP 1-D | O(n) | O(n) or O(1) |
| DP 2-D | O(m × n) | O(m × n) or O(n) |
| Heap push/pop | O(log n) | O(n) |
| Trie insert/search | O(L) | O(L) |
| Union-Find | O(α(n)) ≈ O(1) | O(n) |

---

## Quick Interview Checklist

Before coding:
- [ ] Clarify input constraints (size, sign, duplicates, null/empty?)
- [ ] Ask about expected complexity
- [ ] Walk through 1-2 examples by hand
- [ ] Identify the pattern (use §1 Decision Framework)
- [ ] State your approach + complexity before writing code

While coding:
- [ ] Name variables clearly
- [ ] Handle edge cases (empty, single element, all same)
- [ ] Off-by-one check on loops and slices

After coding:
- [ ] Trace through your example
- [ ] Check edge cases
- [ ] State final time and space complexity

---

*Local files: [baseimplementations/](baseimplementations/) | [structy/](structy/) | [neetcode/](neetcode/) | [algomap/](algomap/)*
