"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Commonly asked at Atlassian

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if 
the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
"""

def isValid(s):
    """
    Time: O(n) where n = length of string
    Space: O(n) for stack
    
    Approach: Use stack to track opening brackets
    """
    # Map closing brackets to opening brackets
    pairs = {')': '(', '}': '{', ']': '['}
    
    stack = []
    
    for char in s:
        if char in pairs:
            # Closing bracket
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            # Opening bracket
            stack.append(char)
    
    # Stack should be empty if all brackets matched
    return len(stack) == 0


def isValid_alternative(s):
    """
    Alternative implementation with explicit checks
    """
    if len(s) % 2 != 0:
        return False
    
    stack = []
    opening = set(['(', '[', '{'])
    
    for char in s:
        if char in opening:
            stack.append(char)
        else:
            if not stack:
                return False
            
            top = stack.pop()
            
            if char == ')' and top != '(':
                return False
            if char == ']' and top != '[':
                return False
            if char == '}' and top != '{':
                return False
    
    return len(stack) == 0


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("((", False),
        ("))", False),
        ("(){}}{", False),
    ]
    
    for s, expected in test_cases:
        result1 = isValid(s)
        result2 = isValid_alternative(s)
        print(f"Input: '{s}'")
        print(f"Output (map): {result1}")
        print(f"Output (alt): {result2}")
        print(f"Expected: {expected}")
        print(f"Pass: {result1 == expected and result2 == expected}\n")
