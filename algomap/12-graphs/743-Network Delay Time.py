# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/

def networkDelayTime(times, n, k):
    """
    You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times
    as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is
    the time it takes for a signal to travel from source to target.
    Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible, return -1.
    
    Args:
        times: List[List[int]]
        n: int
        k: int
        
    Returns:
        int - minimum time
    """
    pass


# Test cases
if __name__ == "__main__":
    print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # Expected: 2
    print(networkDelayTime([[1,2,1]], 2, 1))  # Expected: 1
    print(networkDelayTime([[1,2,1]], 2, 2))  # Expected: -1

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

