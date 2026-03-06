# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def findMin(nums):
    """
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
    Given the sorted rotated array nums of unique elements, return the minimum element of this array.
    
    Args:
        nums: List[int]
        
    Returns:
        int - minimum element
    """
    pass


# Test cases
if __name__ == "__main__":
    print(findMin([3,4,5,1,2]))  # Expected: 1
    print(findMin([4,5,6,7,0,1,2]))  # Expected: 0
    print(findMin([11,13,15,17]))  # Expected: 11
