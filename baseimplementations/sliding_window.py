"""Sliding window patterns.

Run:
    python baseimplementations/sliding_window.py
"""

from __future__ import annotations


def fixed_window_sums(nums: list[int], k: int) -> list[int]:
    """Return sums of each window of size k."""
    if k <= 0:
        raise ValueError("k must be > 0")
    if k > len(nums):
        return []

    res: list[int] = []
    s = sum(nums[:k])
    res.append(s)

    for i in range(k, len(nums)):
        s += nums[i] - nums[i - k]
        res.append(s)

    return res


def longest_subarray_at_most_k_distinct(nums: list[int], k: int) -> int:
    """Variable-size window: longest subarray with <= k distinct values."""
    if k < 0:
        raise ValueError("k must be >= 0")

    freq: dict[int, int] = {}
    left = 0
    best = 0

    for right, x in enumerate(nums):
        freq[x] = freq.get(x, 0) + 1

        while len(freq) > k:
            y = nums[left]
            freq[y] -= 1
            if freq[y] == 0:
                del freq[y]
            left += 1

        best = max(best, right - left + 1)

    return best


def min_subarray_len_at_least_target(nums: list[int], target: int) -> int:
    """Classic variable-size: minimum length with sum >= target (positive nums)."""
    left = 0
    s = 0
    best = float("inf")

    for right, x in enumerate(nums):
        s += x
        while s >= target:
            best = min(best, right - left + 1)
            s -= nums[left]
            left += 1

    return 0 if best == float("inf") else int(best)


def _test_sliding_window() -> None:
    assert fixed_window_sums([1, 2, 3, 4, 5], 3) == [6, 9, 12]
    assert longest_subarray_at_most_k_distinct([1, 2, 1, 2, 3], 2) == 4
    assert min_subarray_len_at_least_target([2, 3, 1, 2, 4, 3], 7) == 2


if __name__ == "__main__":
    _test_sliding_window()
    print("sliding_window.py: OK")
