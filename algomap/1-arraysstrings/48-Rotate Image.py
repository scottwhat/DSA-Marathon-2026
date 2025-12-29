# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/

def rotate(matrix):
    """
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place.
    
    Args:
        matrix: List[List[int]]
        
    Returns:
        None - modifies matrix in-place
    """
    pass


# Test cases
if __name__ == "__main__":
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix1)
    print(matrix1)  # Expected: [[7,4,1],[8,5,2],[9,6,3]]
    
    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rotate(matrix2)
    print(matrix2)  # Expected: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

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

