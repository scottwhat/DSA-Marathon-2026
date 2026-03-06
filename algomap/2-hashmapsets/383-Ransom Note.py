# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/

def canConstruct(ransomNote, magazine):
    """
    Given two strings ransomNote and magazine, return true if ransomNote can be constructed
    by using the letters from magazine and false otherwise.
    
    Args:
        ransomNote: str
        magazine: str
        
    Returns:
        bool - true if can construct ransom note
    """
    pass


# Test cases
if __name__ == "__main__":
    print(canConstruct("a", "b"))  # Expected: False
    print(canConstruct("aa", "ab"))  # Expected: False
    print(canConstruct("aa", "aab"))  # Expected: True
