# 78. Subsets
# https://leetcode.com/problems/subsets/

def subsets(nums):
    """
    Given an integer array nums of unique elements, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.
    
    Args:
        nums: List[int]
        
    Returns:
        List[List[int]] - all subsets
    """
    pass


# Test cases
if __name__ == "__main__":
    print(subsets([1,2,3]))  # Expected: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    print(subsets([0]))  # Expected: [[],[0]]
