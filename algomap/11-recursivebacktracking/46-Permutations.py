# 46. Permutations
# https://leetcode.com/problems/permutations/

def permute(nums):
    """
    Given an array nums of distinct integers, return all the possible permutations.
    You can return the answer in any order.
    
    Args:
        nums: List[int]
        
    Returns:
        List[List[int]] - all permutations
    """
    pass


# Test cases
if __name__ == "__main__":
    print(permute([1,2,3]))  # Expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(permute([0,1]))  # Expected: [[0,1],[1,0]]
