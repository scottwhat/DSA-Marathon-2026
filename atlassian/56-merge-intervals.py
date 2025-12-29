"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

Commonly asked at Atlassian

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

def merge(intervals):
    """
    Time: O(n log n) - sorting
    Space: O(n) - result array
    """
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        current = intervals[i]
        last_merged = merged[-1]
        
        # If current overlaps with last merged interval
        if current[0] <= last_merged[1]:
            # Merge by updating the end of last merged
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap, add as new interval
            merged.append(current)
    
    return merged


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[1,4],[0,4]], [[0,4]]),
        ([[1,4],[2,3]], [[1,4]]),
    ]
    
    for intervals, expected in test_cases:
        result = merge(intervals)
        print(f"Input: {intervals}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")

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

