# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

def isValidSudoku(board):
    """
    Determine if a 9 x 9 Sudoku board is valid.
    
    Args:
        board: List[List[str]]
        
    Returns:
        bool - true if valid
    """
    pass


# Test cases
if __name__ == "__main__":
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(isValidSudoku(board1))  # Expected: True
