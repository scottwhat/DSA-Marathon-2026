# 417. Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/

def pacificAtlantic(heights):
    """
    There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
    The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's
    right and bottom edges. Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that
    rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
    
    Args:
        heights: List[List[int]]
        
    Returns:
        List[List[int]] - coordinates
    """
    pass


# Test cases
if __name__ == "__main__":
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(pacificAtlantic(heights))
    # Expected: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
