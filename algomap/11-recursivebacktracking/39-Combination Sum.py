# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

def combinationSum(candidates, target):
    """
    Given an array of distinct integers candidates and a target integer target, return a list of all unique
    combinations of candidates where the chosen numbers sum to target. The same number may be chosen from
    candidates an unlimited number of times.
    
    Args:
        candidates: List[int]
        target: int
        
    Returns:
        List[List[int]] - all unique combinations
    """
    pass


# Test cases
if __name__ == "__main__":
    print(combinationSum([2,3,6,7], 7))  # Expected: [[2,2,3],[7]]
    print(combinationSum([2,3,5], 8))  # Expected: [[2,2,2,2],[2,3,3],[3,5]]
