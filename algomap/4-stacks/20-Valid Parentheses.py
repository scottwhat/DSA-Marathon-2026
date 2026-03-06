# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

def isValid(s):
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    
    Args:
        s: str
        
    Returns:
        bool - true if valid
    """
    pass


# Test cases
if __name__ == "__main__":
    print(isValid("()"))  # Expected: True
    print(isValid("()[]{}"))  # Expected: True
    print(isValid("(]"))  # Expected: False
