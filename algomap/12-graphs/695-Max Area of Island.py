# 695. Max Area of Island
# https://leetcode.com/problems/max-area-of-island/

def maxAreaOfIsland(grid):
    """
    You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected
    4-directionally. Return the maximum area of an island in grid. If there is no island, return 0.
    
    Args:
        grid: List[List[int]]
        
    Returns:
        int - maximum area
    """
    pass


# Test cases
if __name__ == "__main__":
    grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    print(maxAreaOfIsland(grid))  # Expected: 6
