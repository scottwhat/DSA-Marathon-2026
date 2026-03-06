# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    """
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.
    
    Args:
        nums: List[int]
        
    Returns:
        bool - true if contains duplicate
    """
    pass


# Test cases
if __name__ == "__main__":
    print(containsDuplicate([1,2,3,1]))  # Expected: True
    print(containsDuplicate([1,2,3,4]))  # Expected: False
    print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # Expected: True
