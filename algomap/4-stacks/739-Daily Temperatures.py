# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

def dailyTemperatures(temperatures):
    """
    Given an array of integers temperatures represents the daily temperatures, return an array answer
    such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
    
    Args:
        temperatures: List[int]
        
    Returns:
        List[int] - days to wait for warmer temperature
    """
    pass


# Test cases
if __name__ == "__main__":
    print(dailyTemperatures([73,74,75,71,69,72,76,73]))  # Expected: [1,1,4,2,1,1,0,0]
    print(dailyTemperatures([30,40,50,60]))  # Expected: [1,1,1,0]
