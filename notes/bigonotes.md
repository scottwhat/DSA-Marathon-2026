Order: 
O(1)
O(log N)
O(N)
O(N log N)
O(N²)
O(2^N)
O(N!)

GPT Studying and quizzing - https://chatgpt.com/c/69534ecb-fdb8-8323-bbf3-58152bff8015

Notes:
Big-O keeps the fastest-growing term and deletes everything else.
Time complexity analysis is basically: count how many times the “dominant operation” can happen as input size grows.
The trick: identify the most expensive 

## O(1) - constant
* Notes:
* Use cases:

## O(log N) - log N linear 
* Notes:
- halving, keeps cutting the problem in half
* Use cases:

## O(N) - linear
* Notes:  a straight diagonal line,  one loop n times, two pointers, BFS / DFS over nodes 
* Use cases:

## O(N log N) 
* Notes: Split and do linear work per level, tell tales: sorting, divide and conquer, combine + merge is linear
* Use cases:


## 0(K * log N) K heap ops / K searches
* do a Log N thing * K times Heap push/pop is log(size of heap, size i N or K d
*

## O(N²) - n*n grid
* Notes: nested loops, two loops over the same N, comparing every pair, brute force approaches 
* Use cases:

## O(2^N)
* Notes: choices at every step (1 or 2? ) - backtracking, generating subsets, naive fibonarci recursion without memoisation 

* Use cases: 

## O(N!) - factorial - permutations 
* Notes: N choices, then N-1, then N-2 choices... 
* Use cases: permutations 
*
