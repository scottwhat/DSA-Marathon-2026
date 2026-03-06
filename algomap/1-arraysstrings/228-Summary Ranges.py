# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/

def summaryRanges(nums):
    """
    You are given a sorted unique integer array nums.
    Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
    
    Args:
        nums: List[int]
        
    Returns:
        List[str] - list of ranges
    """
    pass


# Test cases
if __name__ == "__main__":
    print(summaryRanges([0,1,2,4,5,7]))  # Expected: ["0->2","4->5","7"]
    print(summaryRanges([0,2,3,4,6,8,9]))  # Expected: ["0","2->4","6","8->9"]
