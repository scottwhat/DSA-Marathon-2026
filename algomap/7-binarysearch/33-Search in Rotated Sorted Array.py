# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, target):
    """
    There is an integer array nums sorted in ascending order (with distinct values).
    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index.
    Given the array nums after the rotation and an integer target, return the index of target if it is in nums,
    or -1 if it is not in nums.
    
    Args:
        nums: List[int]
        target: int
        
    Returns:
        int - index of target or -1
    """
    pass


# Test cases
if __name__ == "__main__":
    print(search([4,5,6,7,0,1,2], 0))  # Expected: 4
    print(search([4,5,6,7,0,1,2], 3))  # Expected: -1
    print(search([1], 0))  # Expected: -1
