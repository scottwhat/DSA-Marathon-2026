from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent

MARKER = "## Operations & gotchas drill"


def infer_topic(path: Path, text: str) -> str:
    # Prefer folder name, but also look at heading.
    folder = path.parent.name.lower()
    heading = ""
    for line in text.splitlines()[:5]:
        if line.startswith("# Section Summary"):
            heading = line.lower()
            break

    key = f"{folder} {heading}"

    if "atlassian" in key or "system design" in key or "rate limiter" in key:
        return "systems"
    if "array" in key or "string" in key:
        return "arrays"
    if "hash" in key or "set" in key:
        return "hashing"
    if "two pointer" in key or "twopointer" in key or "2pointer" in key:
        return "twopointers"
    if "stack" in key:
        return "stack"
    if "linked" in key:
        return "linkedlist"
    if "binarysearch" in key or "binary search" in key:
        return "binarysearch"
    if "slidingwindow" in key or "sliding window" in key:
        return "slidingwindow"
    if "trie" in key:
        return "trie"
    if "tree" in key and "trie" not in key:
        return "tree"
    if "heap" in key or "priority" in key:
        return "heap"
    if "backtrack" in key or "recursivebacktracking" in key:
        return "backtracking"
    if "graph" in key:
        if "advanced" in key or "graph2" in key:
            return "advancedgraphs"
        return "graph"
    if "dynamic" in key or "dp" in key:
        return "dp"
    if "interval" in key:
        return "intervals"
    if "greedy" in key:
        return "greedy"
    if "bit" in key:
        return "bit"
    if "intro" in key or "introduction" in key:
        return "intro"

    return "general"


def block(topic: str) -> str:
    blocks: dict[str, str] = {
        "arrays": """
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
""",
        "hashing": """
## Operations & gotchas drill
- What are the average-time complexities of: insert, lookup, delete for a hash map? What assumptions are you making?
- Key gotcha: which Python types are hashable/unhashable, and why does mutability matter?
- Collision concept check: what is a collision and why doesn’t it automatically break correctness?
- When using `dict.get(k, 0)`, what bug happens if you forget to write back the increment?
- Frequency-map gotcha: describe the difference between “counting occurrences” and “counting distinct in window” (state maintenance).
- Anagrams key design: compare sorting key vs 26-count tuple (time/space tradeoff).
- Window trick: how do you track “valid window” without rescanning counts each time?
- Set trick: why is `seen.add(x)` in a loop such a common optimization?
- Hashmap trick: when is it useful to map value → index vs value → count?
- Debug drill: if your dict keys look correct but comparisons fail, what should you check (e.g., whitespace, normalization, casing)?

### Quick quiz
1) True/False: Using a tuple of ints as a key is safe in Python.
2) Why can’t you use a list as a dict key?
3) What structure in Python is made for frequency counting?
4) In “two-sum”, why do we store `target - x` or store indices? What is the invariant?
5) What does it mean for a hash table operation to be “amortized” O(1)?
6) True/False: A set preserves insertion order in all languages.
7) When might hashing be worse than sorting in practice?
8) For “longest consecutive sequence”, why does the O(n) set approach work?
""",
        "twopointers": """
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
""",
        "stack": """
## Operations & gotchas drill
- Stack ops drill: what are push/pop/peek complexities in Python using list?
- Valid parentheses: what exactly is stored on the stack and what is the failure condition?
- Monotonic stack gotcha: why store indices instead of values?
- Monotonic invariant: define it precisely for “next greater element” style problems.
- Amortized analysis: why is monotonic stack O(n) even with nested while-loops?
- Parsing trick: how do you handle multi-digit numbers / tokens (e.g., RPN) safely?
- DFS conversion: when converting recursion to an explicit stack, what state must you store?
- Gotcha: when is recursion depth a problem in Python and what do you do instead?

### Quick quiz
1) True/False: A stack can be implemented with a queue in O(1) worst-case per op.
2) What is a “sentinel” value and when does it help in stack problems?
3) Why does each element get popped at most once in a monotonic stack?
4) In daily temperatures, what do you compute when popping an index?
5) What’s the difference between stack and deque in Python use-cases?
6) Name 2 problems where a stack simulates recursion.
""",
        "linkedlist": """
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
""",
        "binarysearch": """
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
""",
        "slidingwindow": """
## Operations & gotchas drill
- Fixed vs variable: name a problem that is fixed window and one that is variable window.
- State maintenance: list 4 window states you might track and the update rules.
- Validity checks: how do you avoid O(n) rescans inside the window?
- Gotcha: when shrinking, what do you update first (state, left pointer, answer)?
- Complexity proof: explain why nested loops can still be O(n) in a correct window.
- Trick: when does “max frequency in window” allow you to avoid shrinking too aggressively?
- Counterexample drill: build an example that breaks a naive window approach.

### Quick quiz
1) True/False: Window problems can always be solved by sorting first.
2) What’s the main difference between “minimum window” and “maximum window” problems?
3) In min-window-substring, what does it mean to be “valid”?
4) Why is moving `left` forward safe once the window is valid?
5) What’s the classic bug with window length calculation?
6) When do you use a deque in sliding window problems?
""",
        "tree": """
## Operations & gotchas drill
- Traversals: write the iterative templates for DFS (stack) and BFS (queue) in words.
- BST gotcha: why checking only `node.left < node < node.right` is insufficient.
- Recursion state: what do you pass down (min/max bounds, path sum, depth) and why?
- Path problems: distinguish root-to-leaf vs any-path and how it changes the algorithm.
- Serialization: what’s the minimal info needed to reconstruct a tree?
- Complexity drill: what is the worst-case height of a BST and why does it matter?
- Trick: how do you do level-order with per-level separation (two loops vs sentinel)?

### Quick quiz
1) True/False: Inorder traversal of a BST is sorted.
2) What makes BFS the natural choice for “shortest path in edges” on a tree?
3) What’s the base case for recursion on a null node?
4) In validating BST, what bounds do you carry?
5) Name a tree problem where postorder is the cleanest approach.
6) What’s the difference between diameter and max path sum?
""",
        "heap": """
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
""",
        "backtracking": """
## Operations & gotchas drill
- Backtracking skeleton: choose → explore → un-choose. What exactly is “un-choose”?
- Duplicate gotcha: how do you prevent repeated combinations/permutations?
- Constraint ordering: why does checking constraints early prune more?
- Complexity drill: estimate runtime using branching factor × depth.
- State bug: what happens if you reuse the same list without copying at the right time?
- Grid DFS gotcha: why must you restore visited state when backtracking?
- Trick: when do you pass an index forward to avoid permutations when you want combinations?

### Quick quiz
1) True/False: Backtracking can often be written iteratively without any stack.
2) What’s pruning? Give one example of a pruning rule.
3) For subsets, how many total subsets exist for n elements?
4) What’s the difference between combinations and permutations in recursion structure?
5) In word search, what makes a partial path invalid?
6) Why is sorting helpful before backtracking in “subsets II”?
""",
        "graph": """
## Operations & gotchas drill
- Representations: adjacency list vs matrix — memory and access tradeoffs.
- Visited gotcha: why do you mark visited when enqueuing in BFS (not when dequeuing)?
- BFS vs DFS: pick one for shortest paths and explain why.
- Directed graph gotcha: what changes in cycle detection vs undirected?
- Grid graphs: what constitutes a node, what are neighbors, and how do you encode coordinates?
- Multi-source BFS: when it’s needed and what the initial queue looks like.
- Union-find: what do path compression and union by rank do?

### Quick quiz
1) True/False: BFS is optimal for weighted graphs.
2) What is the complexity of BFS/DFS in terms of V and E?
3) In course schedule, what does an edge mean semantically?
4) Why do we need a recursion stack / coloring method for directed cycle detection?
5) When is union-find a better fit than BFS/DFS?
6) What’s a common bug when using BFS levels (distance counting)?
""",
        "advancedgraphs": """
## Operations & gotchas drill
- Dijkstra invariant: what is guaranteed when you pop from the heap?
- Negative weights: why Dijkstra fails and what you use instead.
- MST: compare Prim vs Kruskal and where union-find fits.
- Topological sort: what it produces and what a cycle implies.
- Priority queue gotcha: why you may need to ignore stale distances.
- Trick: multi-source BFS vs Dijkstra—when each applies.

### Quick quiz
1) True/False: Bellman-Ford can detect negative cycles.
2) What’s the difference between shortest path tree and MST?
3) In Kruskal, what’s the greedy choice?
4) What does in-degree represent in Kahn’s algorithm?
5) Why do we sometimes push multiple entries per node into the PQ?
6) When would you use Floyd-Warshall?
""",
        "dp": """
## Operations & gotchas drill
- State-definition drill: define state in one sentence for a DP problem you know.
- Transition drill: write the recurrence and explain each term.
- Base-case gotcha: why missing base cases silently breaks correctness.
- Memo vs tab: when is recursion+memo easier and when is tabulation safer?
- Space optimization: when rolling arrays work (dependency only on previous row/col).
- Trick: how do you detect whether DP is overkill (subproblems don’t overlap)?
- Debug trick: print small dp tables for tiny inputs.

### Quick quiz
1) True/False: DP always improves time complexity.
2) What does `dp[i]` typically mean in 1D DP?
3) In 2D DP, what does `dp[r][c]` usually represent?
4) Give one example of unbounded knapsack.
5) What is “optimal substructure”?
6) Why can LIS be done in O(n log n) (high-level)?
""",
        "trie": """
## Operations & gotchas drill
- Operations: insert/search/startsWith — what is their time in terms of word length?
- Memory gotcha: why tries can be memory heavy; what compressions exist (map children, radix tree).
- Word search: what’s the pruning condition using trie?
- Duplicate results: how do you avoid returning the same word multiple times?
- Implementation gotcha: when do you mark end-of-word and how do you store full words efficiently?

### Quick quiz
1) True/False: Trie operations depend on number of stored words.
2) What does an end-of-word marker enable?
3) Why is trie good for prefix queries?
4) In DFS + trie, what makes a branch dead early?
5) Name one alternative structure for prefix search.
""",
        "intervals": """
## Operations & gotchas drill
- Sorting gotcha: when merging, why do we sort by start then compare ends?
- Endpoint gotcha: inclusive vs exclusive endpoints; how does it change overlap condition?
- Meeting rooms II: what does the min-heap store and why is it correct?
- Greedy scheduling: why sorting by end time is the classic optimal choice.
- Trick: how do you treat equal start times (tie-breaker by end)?

### Quick quiz
1) True/False: Intervals can always be merged without sorting.
2) What’s the overlap condition if intervals are closed [a,b] and [c,d]?
3) In meeting rooms, what indicates you can reuse a room?
4) Why does sorting by end time help maximize number of non-overlapping intervals?
5) Name a tricky case involving touching endpoints.
""",
        "greedy": """
## Operations & gotchas drill
- Greedy proof drill: what’s the exchange argument in plain English?
- Counterexample drill: how do you test whether a greedy choice might fail?
- Sorting trick: many greedy solutions rely on sorting—what property does sorting create?
- Jump game: define the invariant behind tracking farthest reach.
- Gas station: why can you discard earlier start indices after tank dips negative?

### Quick quiz
1) True/False: Greedy always works if it feels right.
2) What is the difference between local optimal and global optimal?
3) Give one standard way to prove greedy correctness.
4) In interval scheduling, what is the greedy choice?
5) Name a greedy problem that is actually DP if constraints change.
""",
        "bit": """
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
""",
        "intro": """
## Operations & gotchas drill
- Given a problem, list the first 5 questions you ask before writing code.
- Complexity drill: distinguish worst-case vs average-case vs amortized.
- Edge-case drill: empty input, 1 element, duplicates, negative numbers, large values.
- Debug drill: what’s your minimal reproducible failing test strategy?
- Communication drill: how do you narrate your approach in an interview?

### Quick quiz
1) True/False: If you pass all sample tests, you’re done.
2) What’s the difference between time complexity and runtime?
3) Give one example where optimizing space hurts readability but is worth it.
4) What’s a good sign you should use hashing?
5) What’s a good sign you should use BFS?
""",
        "systems": """
## Operations & gotchas drill
- Rate limiter: compare fixed window, sliding window, token bucket—what’s the main gotcha for each?
- Time gotcha: clock skew and distributed systems—how does it affect rate limiting?
- Idempotency: define it and explain why retries require it.
- Data structures: for LRU, what operations must be O(1) and how do you achieve that?
- Scheduler: what happens if a worker crashes mid-job? What state transitions are needed?
- Consistency drill: what do you store (in-memory vs persistent) and why?
- Load drill: what metrics indicate backpressure is needed?

### Quick quiz
1) True/False: Using Redis automatically solves distributed locking issues.
2) In a token bucket, what does “burst” mean?
3) What’s the difference between at-least-once and exactly-once processing?
4) Name two ways to implement delayed jobs.
5) What’s a common pitfall of fixed-window rate limiting?
6) In an LRU cache, what do you update on every `get`?
""",
        "general": """
## Operations & gotchas drill
- Pick the top 3 data structures you’d try first and justify each.
- Identify 5 edge cases you test by default.
- List 3 invariants you could track to prove correctness.

### Quick quiz
1) True/False: Most bugs are edge-case related.
2) What is an invariant and why does it matter?
3) Give one example of trading space for time.
""",
    }

    return blocks.get(topic, blocks["general"]).lstrip("\n")


def enrich(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        return False

    topic = infer_topic(path, text)
    addition = block(topic)

    # normalize ending newlines before appending
    if not text.endswith("\n"):
        text += "\n"
    if not text.endswith("\n\n"):
        text += "\n"

    text += addition
    path.write_text(text, encoding="utf-8")
    return True


def main() -> None:
    updated = 0
    for p in REPO_ROOT.rglob("sectionsummary.md"):
        parts = {x.lower() for x in p.parts}
        if ".git" in parts or "__pycache__" in parts:
            continue
        if enrich(p):
            updated += 1

    print(f"Updated {updated} files")


if __name__ == "__main__":
    main()
