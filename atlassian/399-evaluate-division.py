"""
399. Evaluate Division
https://leetcode.com/problems/evaluate-division/

Commonly asked at Atlassian

You are given an array of variable pairs equations and an array of real numbers values, where 
equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi 
is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you 
must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in 
division by zero and that there is no contradiction.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], 
       queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
"""

from collections import defaultdict, deque

def calcEquation_BFS(equations, values, queries):
    """
    Time: O(M * N) where M = number of queries, N = number of equations
    Space: O(N)
    
    Approach: Build graph and use BFS to find path between nodes
    """
    # Build graph: node -> [(neighbor, weight)]
    graph = defaultdict(list)
    
    for (dividend, divisor), value in zip(equations, values):
        graph[dividend].append((divisor, value))
        graph[divisor].append((dividend, 1.0 / value))
    
    def bfs(start, end):
        """Find path from start to end and return product of weights"""
        if start not in graph or end not in graph:
            return -1.0
        
        if start == end:
            return 1.0
        
        queue = deque([(start, 1.0)])  # (node, accumulated_product)
        visited = {start}
        
        while queue:
            node, product = queue.popleft()
            
            if node == end:
                return product
            
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, product * weight))
        
        return -1.0
    
    return [bfs(start, end) for start, end in queries]


def calcEquation_DFS(equations, values, queries):
    """
    Alternative: DFS approach
    Time: O(M * N)
    Space: O(N)
    """
    graph = defaultdict(list)
    
    for (dividend, divisor), value in zip(equations, values):
        graph[dividend].append((divisor, value))
        graph[divisor].append((dividend, 1.0 / value))
    
    def dfs(start, end, visited):
        """Find path from start to end using DFS"""
        if start not in graph or end not in graph:
            return -1.0
        
        if start == end:
            return 1.0
        
        visited.add(start)
        
        for neighbor, weight in graph[start]:
            if neighbor not in visited:
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return weight * result
        
        return -1.0
    
    return [dfs(start, end, set()) for start, end in queries]


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "equations": [["a","b"],["b","c"]],
            "values": [2.0, 3.0],
            "queries": [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]],
            "expected": [6.0, 0.5, -1.0, 1.0, -1.0]
        },
        {
            "equations": [["a","b"],["b","c"],["bc","cd"]],
            "values": [1.5, 2.5, 5.0],
            "queries": [["a","c"],["c","b"],["bc","cd"],["cd","bc"]],
            "expected": [3.75, 0.4, 5.0, 0.2]
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"=== Test {i} ===")
        equations = test["equations"]
        values = test["values"]
        queries = test["queries"]
        expected = test["expected"]
        
        result_bfs = calcEquation_BFS(equations, values, queries)
        result_dfs = calcEquation_DFS(equations, values, queries)
        
        print(f"Equations: {equations}")
        print(f"Values: {values}")
        print(f"Queries: {queries}")
        print(f"BFS Result: {result_bfs}")
        print(f"DFS Result: {result_dfs}")
        print(f"Expected: {expected}")
        print()
