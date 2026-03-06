# 15. 3Sum
# https://leetcode.com/problems/3sum/

def threeSum(nums):
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
    i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    
    Args:
        nums: List[int]
        
    Returns:
        List[List[int]] - list of triplets
    """
    pass


# Test cases
if __name__ == "__main__":
    print(threeSum([-1,0,1,2,-1,-4]))  # Expected: [[-1,-1,2],[-1,0,1]]
    print(threeSum([0,1,1]))  # Expected: []
    print(threeSum([0,0,0]))  # Expected: [[0,0,0]]
