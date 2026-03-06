# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

def numIslands(grid):
    """
    Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
    return the number of islands.
    
    Args:
        grid: List[List[str]]
        
    Returns:
        int - number of islands
    """
    pass


# Test cases
if __name__ == "__main__":
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(numIslands(grid1))  # Expected: 1
    
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(numIslands(grid2))  # Expected: 3
