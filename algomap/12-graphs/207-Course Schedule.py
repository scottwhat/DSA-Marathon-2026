# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

def canFinish(numCourses, prerequisites):
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
    take course bi first if you want to take course ai.
    Return true if you can finish all courses. Otherwise, return false.
    
    Args:
        numCourses: int
        prerequisites: List[List[int]]
        
    Returns:
        bool - true if can finish all courses
    """
    pass


# Test cases
if __name__ == "__main__":
    print(canFinish(2, [[1,0]]))  # Expected: True
    print(canFinish(2, [[1,0],[0,1]]))  # Expected: False
