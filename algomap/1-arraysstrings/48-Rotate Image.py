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
