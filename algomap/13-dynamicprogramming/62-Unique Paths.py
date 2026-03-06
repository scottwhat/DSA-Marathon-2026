# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/

def uniquePaths(m, n):
    """
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
    The robot can only move either down or right at any point in time.
    Given the two integers m and n, return the number of possible unique paths that the robot can take
    to reach the bottom-right corner.
    
    Args:
        m: int - rows
        n: int - columns
        
    Returns:
        int - number of unique paths
    """
    pass


# Test cases
if __name__ == "__main__":
    print(uniquePaths(3, 7))  # Expected: 28
    print(uniquePaths(3, 2))  # Expected: 3
