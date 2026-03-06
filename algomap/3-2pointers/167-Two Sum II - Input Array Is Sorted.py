# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def twoSum(numbers, target):
    """
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
    find two numbers such that they add up to a specific target number.
    
    Args:
        numbers: List[int]
        target: int
        
    Returns:
        List[int] - 1-indexed positions of the two numbers
    """
    pass


# Test cases
if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))  # Expected: [1,2]
    print(twoSum([2,3,4], 6))  # Expected: [1,3]
    print(twoSum([-1,0], -1))  # Expected: [1,2]
