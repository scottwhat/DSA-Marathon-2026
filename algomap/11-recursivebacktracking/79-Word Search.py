# 79. Word Search
# https://leetcode.com/problems/word-search/

def exist(board, word):
    """
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
    horizontally or vertically neighboring.
    
    Args:
        board: List[List[str]]
        word: str
        
    Returns:
        bool - true if word exists
    """
    pass


# Test cases
if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(exist(board, "ABCCED"))  # Expected: True
    print(exist(board, "SEE"))     # Expected: True
    print(exist(board, "ABCB"))    # Expected: False
