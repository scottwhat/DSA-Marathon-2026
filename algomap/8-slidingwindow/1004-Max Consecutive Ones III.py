# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/

def longestOnes(nums, k):
    """
    Given a binary array nums and an integer k, return the maximum number of consecutive 1's
    in the array if you can flip at most k 0's.
    
    Args:
        nums: List[int]
        k: int
        
    Returns:
        int - maximum consecutive ones
    """
    pass


# Test cases
if __name__ == "__main__":
    print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # Expected: 6
    print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))  # Expected: 10
