# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

def groupAnagrams(strs):
    """
    Given an array of strings strs, group the anagrams together.
    
    Args:
        strs: List[str]
        
    Returns:
        List[List[str]] - grouped anagrams
    """
    pass


# Test cases
if __name__ == "__main__":
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # Expected: [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(groupAnagrams([""]))  # Expected: [[""]]
    print(groupAnagrams(["a"]))  # Expected: [["a"]]
