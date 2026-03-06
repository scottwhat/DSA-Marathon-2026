# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/

def searchMatrix(matrix, target):
    """
    You are given an m x n integer matrix with the following properties:
    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.
    Given an integer target, return true if target is in matrix or false otherwise.
    
    Args:
        matrix: List[List[int]]
        target: int
        
    Returns:
        bool - true if target exists
    """
    pass


# Test cases
if __name__ == "__main__":
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # Expected: True
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))  # Expected: False
