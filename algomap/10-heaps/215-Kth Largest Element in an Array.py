# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

def findKthLargest(nums, k):
    """
    Given an integer array nums and an integer k, return the kth largest element in the array.
    Note that it is the kth largest element in the sorted order, not the kth distinct element.
    
    Args:
        nums: List[int]
        k: int
        
    Returns:
        int - kth largest element
    """
    pass


# Test cases
if __name__ == "__main__":
    print(findKthLargest([3,2,1,5,6,4], 2))  # Expected: 5
    print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # Expected: 4
