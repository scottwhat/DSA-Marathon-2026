# 322. Coin Change
# https://leetcode.com/problems/coin-change/

def coinChange(coins, amount):
    """
    You are given an integer array coins representing coins of different denominations and an integer
    amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount. If that amount of money
    cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.
    
    Args:
        coins: List[int]
        amount: int
        
    Returns:
        int - fewest number of coins or -1
    """
    pass


# Test cases
if __name__ == "__main__":
    print(coinChange([1,2,5], 11))  # Expected: 3
    print(coinChange([2], 3))  # Expected: -1
    print(coinChange([1], 0))  # Expected: 0
