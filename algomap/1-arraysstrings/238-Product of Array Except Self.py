# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

def productExceptSelf(nums):
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to
    the product of all the elements of nums except nums[i].
    
    Args:
        nums: List[int]
        
    Returns:
        List[int] - product array
    """
    pass


# Test cases
if __name__ == "__main__":
    print(productExceptSelf([1,2,3,4]))    # Expected: [24,12,8,6]
    print(productExceptSelf([-1,1,0,-3,3]))  # Expected: [0,0,9,0,0]
