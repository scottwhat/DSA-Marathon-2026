# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

## brute force
## top down recursive + memoisation - dfs with caching - subproblem is, 
# start, all sub sequences with indexes increasing 
# i need to s

## bottom up has the same recurrence relation 
## 

def longest_sub_len(nums: list[int]) -> int:
    n = len(nums)

    ## make dp array
    dp = [0] * (n + 1)

    ## set base case 
    dp[0] = 0  # base case: no elements has an LIS of length 0
    max_len = 0

    
    for i in range(1, n + 1):
        ni = nums[i - 1]

        # first we try starting a new sequence
        dp[i] = dp[0] + 1
        # then try extending an existing LIS from indices less than i

        #j will be the second loop index, and begins again each 
        for j in range(1, i):
            nj = nums[j - 1]
            if nj < ni:
                dp[i] = max(dp[i], dp[j] + 1)

        max_len = max(max_len, dp[i])

    return max_len

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    res = longest_sub_len(nums)
    print(res)
