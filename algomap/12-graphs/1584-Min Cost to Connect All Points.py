# 1584. Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/

def minCostConnectPoints(points):
    """
    You are given an array points representing integer coordinates of some points on a 2D-plane,
    where points[i] = [xi, yi]. The cost of connecting two points is the manhattan distance between them.
    Return the minimum cost to make all points connected.
    
    Args:
        points: List[List[int]]
        
    Returns:
        int - minimum cost
    """
    pass


# Test cases
if __name__ == "__main__":
    print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))  # Expected: 20
    print(minCostConnectPoints([[3,12],[-2,5],[-4,1]]))  # Expected: 18
