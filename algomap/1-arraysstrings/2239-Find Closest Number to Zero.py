# 2239. Find Closest Number to Zero
# https://leetcode.com/problems/find-closest-number-to-zero/

def findClosestNumber(nums):
    """
    Given an integer array nums of size n, return the number with the value closest to 0 in nums.
    If there are multiple answers, return the number with the largest value.
    
    Args:
        nums: List[int] - array of integers
        
    Returns:
        int - the number closest to 0
    """
    pass


# Test cases
if __name__ == "__main__":
    # Example 1
    nums1 = [-4, -2, 1, 4, 8]
    print(f"Input: {nums1}")
    print(f"Output: {findClosestNumber(nums1)}")
    # Expected: 1
    
    # Example 2
    nums2 = [2, -1, 1]
    print(f"\nInput: {nums2}")
    print(f"Output: {findClosestNumber(nums2)}")
    # Expected: 1
