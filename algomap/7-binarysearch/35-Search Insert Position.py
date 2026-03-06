# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/

def searchInsert(nums, target):
    """
    Given a sorted array of distinct integers and a target value, return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.
    
    Args:
        nums: List[int]
        target: int
        
    Returns:
        int - index
    """
    pass


# Test cases
if __name__ == "__main__":
    print(searchInsert([1,3,5,6], 5))  # Expected: 2
    print(searchInsert([1,3,5,6], 2))  # Expected: 1
    print(searchInsert([1,3,5,6], 7))  # Expected: 4
