# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1
        

        prev = 1
        curr = 2

        for i in range(2, n):
            temp = prev
            prev = curr
            curr = curr + temp 

        return curr
