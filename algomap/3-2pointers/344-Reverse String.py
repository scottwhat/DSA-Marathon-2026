# 344. Reverse String
# https://leetcode.com/problems/reverse-string/

def reverseString(s):
    """
    Write a function that reverses a string. The input string is given as an array of characters s.
    You must do this by modifying the input array in-place with O(1) extra memory.
    
    Args:
        s: List[str]
        
    Returns:
        None - modifies s in-place
    """
    pass


# Test cases
if __name__ == "__main__":
    s1 = ["h","e","l","l","o"]
    reverseString(s1)
    print(s1)  # Expected: ["o","l","l","e","h"]
    
    s2 = ["H","a","n","n","a","h"]
    reverseString(s2)
    print(s2)  # Expected: ["h","a","n","n","a","H"]
