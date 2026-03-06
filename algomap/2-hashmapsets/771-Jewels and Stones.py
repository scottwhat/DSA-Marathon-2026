# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

def numJewelsInStones(jewels, stones):
    """
    You're given strings jewels representing the types of stones that are jewels, and stones representing
    the stones you have. Each character in stones is a type of stone you have. You want to know how many
    of the stones you have are also jewels.
    
    Args:
        jewels: str
        stones: str
        
    Returns:
        int - number of jewels
    """
    pass


# Test cases
if __name__ == "__main__":
    print(numJewelsInStones("aA", "aAAbbbb"))  # Expected: 3
    print(numJewelsInStones("z", "ZZ"))  # Expected: 0
