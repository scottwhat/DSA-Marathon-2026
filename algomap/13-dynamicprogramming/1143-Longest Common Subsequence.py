# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/

def longestCommonSubsequence(text1, text2):
    """
    Given two strings text1 and text2, return the length of their longest common subsequence.
    If there is no common subsequence, return 0.
    A subsequence of a string is a new string generated from the original string with some characters
    (can be none) deleted without changing the relative order of the remaining characters.
    
    Args:
        text1: str
        text2: str
        
    Returns:
        int - length of longest common subsequence
    """
    pass


# Test cases
if __name__ == "__main__":
    print(longestCommonSubsequence("abcde", "ace"))  # Expected: 3
    print(longestCommonSubsequence("abc", "abc"))  # Expected: 3
    print(longestCommonSubsequence("abc", "def"))  # Expected: 0
