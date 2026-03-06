# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/

def minEatingSpeed(piles, h):
    """
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas
    and eats k bananas from that pile.
    Return the minimum integer k such that she can eat all the bananas within h hours.
    
    Args:
        piles: List[int]
        h: int
        
    Returns:
        int - minimum eating speed
    """
    pass


# Test cases
if __name__ == "__main__":
    print(minEatingSpeed([3,6,7,11], 8))  # Expected: 4
    print(minEatingSpeed([30,11,23,4,20], 5))  # Expected: 30
    print(minEatingSpeed([30,11,23,4,20], 6))  # Expected: 23
