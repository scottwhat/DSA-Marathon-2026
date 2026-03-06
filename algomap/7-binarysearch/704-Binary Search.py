# 704. Binary Search
# https://leetcode.com/problems/binary-search/

def search(nums, target):
    """
    Given an array of integers nums which is sorted in ascending order, and an integer target,
    write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
    
    Args:
        nums: List[int]
        target: int
        
    Returns:
        int - index of target or -1
    """
    pass


# Test cases
if __name__ == "__main__":
    print(search([-1,0,3,5,9,12], 9))  # Expected: 4
    print(search([-1,0,3,5,9,12], 2))  # Expected: -1
