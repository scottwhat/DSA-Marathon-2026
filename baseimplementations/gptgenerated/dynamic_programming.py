"""Dynamic programming patterns: memoization + tabulation templates.

Run:
    python baseimplementations/dynamic_programming.py
"""

from __future__ import annotations

from functools import lru_cache


def fib_memo(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")

    @lru_cache(maxsize=None)
    def dp(i: int) -> int:
        if i <= 1:
            return i
        return dp(i - 1) + dp(i - 2)

    return dp(n)


def fib_tab(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def coin_change_min_coins(amount: int, coins: list[int]) -> int:
    """Bottom-up: min coins to make amount. Returns -1 if impossible."""
    if amount < 0:
        raise ValueError("amount must be >= 0")
    if amount == 0:
        return 0

    INF = 10**9
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a - c] + 1)

    return -1 if dp[amount] >= INF else dp[amount]


def knapsack_01_max_value(capacity: int, weights: list[int], values: list[int]) -> int:
    """0/1 knapsack (tabulation)."""
    if len(weights) != len(values):
        raise ValueError("weights and values must have same length")

    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        w, v = weights[i], values[i]
        for cap in range(capacity, w - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - w] + v)
    return dp[capacity]


def _test_dynamic_programming() -> None:
    assert fib_memo(10) == 55
    assert fib_tab(10) == 55
    assert coin_change_min_coins(11, [1, 2, 5]) == 3
    assert coin_change_min_coins(3, [2]) == -1
    assert knapsack_01_max_value(7, [1, 3, 4, 5], [1, 4, 5, 7]) == 9


if __name__ == "__main__":
    _test_dynamic_programming()
    print("dynamic_programming.py: OK")
