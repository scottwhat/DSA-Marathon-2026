# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/

class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
    """
    A linked list of length n is given such that each node contains an additional random pointer.
    Construct a deep copy of the list.
    
    Args:
        head: Node
        
    Returns:
        Node - head of copied list
    """
    pass


# Test cases
if __name__ == "__main__":
    # Example: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    pass
