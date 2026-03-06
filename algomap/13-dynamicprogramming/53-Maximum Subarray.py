# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums):
    """
    Given an integer array nums, find the subarray with the largest sum, and return its sum.
    This problem uses Kadane's Algorithm.
    
    Args:
        nums: List[int]
        
    Returns:
        int - maximum sum
    """
    pass


# Test cases
if __name__ == "__main__":
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Expected: 6
    print(maxSubArray([1]))  # Expected: 1
    print(maxSubArray([5,4,-1,7,8]))  # Expected: 23
