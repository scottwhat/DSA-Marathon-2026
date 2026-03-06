# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/

def findOrder(numCourses, prerequisites):
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
    Some courses may have prerequisites. Return the ordering of courses you should take to finish all courses.
    If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
    
    Args:
        numCourses: int
        prerequisites: List[List[int]]
        
    Returns:
        List[int] - course order
    """
    pass


# Test cases
if __name__ == "__main__":
    print(findOrder(2, [[1,0]]))  # Expected: [0,1]
    print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))  # Expected: [0,2,1,3] or [0,1,2,3]
