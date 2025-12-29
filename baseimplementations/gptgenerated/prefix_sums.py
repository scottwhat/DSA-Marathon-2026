"""Prefix sums patterns.

Run:
    python baseimplementations/prefix_sums.py
"""

from __future__ import annotations


def build_prefix_sums(nums: list[int]) -> list[int]:
    """Returns prefix sums with leading 0, so sum(i..j)=ps[j+1]-ps[i]."""
    ps = [0]
    s = 0
    for x in nums:
        s += x
        ps.append(s)
    return ps


def range_sum(prefix: list[int], i: int, j: int) -> int:
    return prefix[j + 1] - prefix[i]


def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    """Count subarrays summing to k (prefix sum + hashmap)."""
    count = 0
    prefix = 0
    seen = {0: 1}
    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count


def _test_prefix_sums() -> None:
    nums = [1, 2, 3, 4]
    ps = build_prefix_sums(nums)
    assert ps == [0, 1, 3, 6, 10]
    assert range_sum(ps, 1, 2) == 5
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2


if __name__ == "__main__":
    _test_prefix_sums()
    print("prefix_sums.py: OK")
