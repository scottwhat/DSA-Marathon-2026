# 155. Min Stack
# https://leetcode.com/problems/min-stack/

class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    """
    
    def __init__(self):
        pass
        
    def push(self, val: int) -> None:
        pass
        
    def pop(self) -> None:
        pass
        
    def top(self) -> int:
        pass
        
    def getMin(self) -> int:
        pass


# Test cases
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # Expected: -3
    minStack.pop()
    print(minStack.top())     # Expected: 0
    print(minStack.getMin())  # Expected: -2
