"""
1091. Shortest Path in Binary Matrix
https://leetcode.com/problems/shortest-path-in-binary-matrix/

Commonly asked at Atlassian

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. 
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the 
bottom-right cell (i.e., (n - 1, n - 1)) such that:
- All the visited cells of the path are 0.
- All the adjacent cells of the path are 8-directionally connected (i.e., they are different 
  and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
"""

from collections import deque

def shortestPathBinaryMatrix(grid):
    """
    Time: O(n^2) where n = side length of grid
    Space: O(n^2)
    
    Approach: BFS with 8-directional movement
    """
    n = len(grid)
    
    # Check if start or end is blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    # Special case: single cell
    if n == 1:
        return 1
    
    # 8 directions: up, down, left, right, and 4 diagonals
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    visited = {(0, 0)}
    
    while queue:
        row, col, dist = queue.popleft()
        
        # Check if we reached the end
        if row == n-1 and col == n-1:
            return dist
        
        # Explore all 8 directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check bounds and if cell is valid
            if (0 <= new_row < n and 0 <= new_col < n and 
                grid[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))
    
    return -1


def shortestPathBinaryMatrix_AStar(grid):
    """
    Alternative: A* search with Manhattan distance heuristic
    Time: O(n^2 log n^2) = O(n^2 log n)
    Space: O(n^2)
    """
    import heapq
    
    n = len(grid)
    
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    if n == 1:
        return 1
    
    def heuristic(row, col):
        """Chebyshev distance (max of abs differences) for 8-directional"""
        return max(abs(row - (n-1)), abs(col - (n-1)))
    
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    # Priority queue: (f_score, g_score, row, col)
    pq = [(1 + heuristic(0, 0), 1, 0, 0)]
    visited = {(0, 0)}
    
    while pq:
        f_score, g_score, row, col = heapq.heappop(pq)
        
        if row == n-1 and col == n-1:
            return g_score
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < n and 0 <= new_col < n and 
                grid[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                new_g = g_score + 1
                new_f = new_g + heuristic(new_row, new_col)
                heapq.heappush(pq, (new_f, new_g, new_row, new_col))
    
    return -1


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[0,1],[1,0]], 2),
        ([[0,0,0],[1,1,0],[1,1,0]], 4),
        ([[1,0,0],[1,1,0],[1,1,0]], -1),
        ([[0]], 1),
        ([[0,0,0],[0,1,0],[0,0,0]], 4),
    ]
    
    for grid, expected in test_cases:
        result1 = shortestPathBinaryMatrix([row[:] for row in grid])
        result2 = shortestPathBinaryMatrix_AStar([row[:] for row in grid])
        print(f"Grid: {grid}")
        print(f"BFS Result: {result1}")
        print(f"A* Result: {result2}")
        print(f"Expected: {expected}")
        print(f"Pass: {result1 == expected and result2 == expected}\n")

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

