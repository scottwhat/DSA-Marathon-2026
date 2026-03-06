# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s):
    """
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
    and removing all non-alphanumeric characters, it reads the same forward and backward.
    
    Args:
        s: str
        
    Returns:
        bool - true if palindrome
    """
    pass


# Test cases
if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))  # Expected: True
    print(isPalindrome("race a car"))  # Expected: False
    print(isPalindrome(" "))  # Expected: True
