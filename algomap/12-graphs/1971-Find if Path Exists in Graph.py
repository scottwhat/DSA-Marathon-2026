# 1971. Find if Path Exists in Graph
# https://leetcode.com/problems/find-if-path-exists-in-graph/

def validPath(n, edges, source, destination):
    """
    There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1.
    Given n, edges, and two nodes source and destination, return true if there is a valid path from source to destination.
    
    Args:
        n: int
        edges: List[List[int]]
        source: int
        destination: int
        
    Returns:
        bool - true if path exists
    """
    pass


# Test cases
if __name__ == "__main__":
    print(validPath(3, [[0,1],[1,2],[2,0]], 0, 2))  # Expected: True
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))  # Expected: False
