# 1971. Find if Path Exists in Graph
# https://leetcode.com/problems/find-if-path-exists-in-graph/

def validPath(n, edges, source, destination):
    """
    There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1.
    Given n, edges, and two nodes source and destination, return true if there is a valid path from source to destination.
    
    Args:
        n: int
        edges: List[List[int]]
        source: int
        destination: int
        
    Returns:
        bool - true if path exists
    """
    pass


# Test cases
if __name__ == "__main__":
    print(validPath(3, [[0,1],[1,2],[2,0]], 0, 2))  # Expected: True
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))  # Expected: False

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

