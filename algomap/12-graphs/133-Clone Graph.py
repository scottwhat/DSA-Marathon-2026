# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    """
    Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
    
    Args:
        node: Node
        
    Returns:
        Node - cloned graph
    """
    pass


# Test cases
if __name__ == "__main__":
    # Example: adjList = [[2,4],[1,3],[2,4],[1,3]]
    pass
