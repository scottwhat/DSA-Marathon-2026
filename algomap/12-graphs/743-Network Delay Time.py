# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/

def networkDelayTime(times, n, k):
    """
    You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times
    as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is
    the time it takes for a signal to travel from source to target.
    Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible, return -1.
    
    Args:
        times: List[List[int]]
        n: int
        k: int
        
    Returns:
        int - minimum time
    """
    pass


# Test cases
if __name__ == "__main__":
    print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # Expected: 2
    print(networkDelayTime([[1,2,1]], 2, 1))  # Expected: 1
    print(networkDelayTime([[1,2,1]], 2, 2))  # Expected: -1
