# 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/

def mergeAlternately(word1, word2):
    """
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
    starting with word1. If a string is longer than the other, append the additional letters onto the end
    of the merged string.
    
    Args:
        word1: str
        word2: str
        
    Returns:
        str - merged string
    """
    pass


# Test cases
if __name__ == "__main__":
    print(mergeAlternately("abc", "pqr"))  # Expected: "apbqcr"
    print(mergeAlternately("ab", "pqrs"))  # Expected: "apbqrs"
    print(mergeAlternately("abcd", "pq"))  # Expected: "apbqcd"
