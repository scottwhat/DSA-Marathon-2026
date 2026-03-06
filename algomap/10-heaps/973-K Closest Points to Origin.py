# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/

def kClosest(points, k):
    """
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
    return the k closest points to the origin (0, 0).
    
    Args:
        points: List[List[int]]
        k: int
        
    Returns:
        List[List[int]] - k closest points
    """
    pass


# Test cases
if __name__ == "__main__":
    print(kClosest([[1,3],[-2,2]], 1))  # Expected: [[-2,2]]
    print(kClosest([[3,3],[5,-1],[-2,4]], 2))  # Expected: [[3,3],[-2,4]]
