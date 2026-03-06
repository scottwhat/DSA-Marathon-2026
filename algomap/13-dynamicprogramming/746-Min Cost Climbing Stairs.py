# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

def minCostClimbingStairs(cost):
    """
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
    Once you pay the cost, you can either climb one or two steps.
    You can either start from the step with index 0, or the step with index 1.
    Return the minimum cost to reach the top of the floor.
    
    Args:
        cost: List[int]
        
    Returns:
        int - minimum cost
    """
    pass


# Test cases
if __name__ == "__main__":
    print(minCostClimbingStairs([10,15,20]))  # Expected: 15
    print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))  # Expected: 6
