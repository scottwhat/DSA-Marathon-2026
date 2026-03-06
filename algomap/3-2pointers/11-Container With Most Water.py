# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
    """
    You are given an integer array height of length n. There are n vertical lines drawn such that
    the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container that contains the most water.
    
    Args:
        height: List[int]
        
    Returns:
        int - maximum area
    """
    pass


# Test cases
if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))  # Expected: 49
    print(maxArea([1,1]))  # Expected: 1
