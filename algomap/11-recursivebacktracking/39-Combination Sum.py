# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

def combinationSum(candidates, target):
    """
    Given an array of distinct integers candidates and a target integer target, return a list of all unique
    combinations of candidates where the chosen numbers sum to target. The same number may be chosen from
    candidates an unlimited number of times.
    
    Args:
        candidates: List[int]
        target: int
        
    Returns:
        List[List[int]] - all unique combinations
    """
    pass


# Test cases
if __name__ == "__main__":
    print(combinationSum([2,3,6,7], 7))  # Expected: [[2,2,3],[7]]
    print(combinationSum([2,3,5], 8))  # Expected: [[2,2,2,2],[2,3,3],[3,5]]

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

