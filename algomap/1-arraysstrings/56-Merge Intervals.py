# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

def merge(intervals):
    """
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals.
    
    Args:
        intervals: List[List[int]]
        
    Returns:
        List[List[int]] - merged intervals
    """
    pass


# Test cases
if __name__ == "__main__":
    print(merge([[1,3],[2,6],[8,10],[15,18]]))  # Expected: [[1,6],[8,10],[15,18]]
    print(merge([[1,4],[4,5]]))  # Expected: [[1,5]]
