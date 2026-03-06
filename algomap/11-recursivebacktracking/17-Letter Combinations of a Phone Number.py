# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def letterCombinations(digits):
    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations
    that the number could represent. Return the answer in any order.
    
    Args:
        digits: str
        
    Returns:
        List[str] - all letter combinations
    """
    pass


# Test cases
if __name__ == "__main__":
    print(letterCombinations("23"))  # Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(letterCombinations(""))    # Expected: []
    print(letterCombinations("2"))   # Expected: ["a","b","c"]
