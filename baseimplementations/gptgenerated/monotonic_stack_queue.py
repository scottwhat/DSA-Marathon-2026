"""Monotonic stack / monotonic queue patterns.

Run:
    python baseimplementations/monotonic_stack_queue.py
"""

from __future__ import annotations

from collections import deque
from typing import Deque


def next_greater_elements(nums: list[int]) -> list[int]:
    """For each element, find next greater to the right; -1 if none."""
    res = [-1] * len(nums)
    st: list[int] = []  # stack of indices, decreasing by value
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            j = st.pop()
            res[j] = x
        st.append(i)
    return res


def sliding_window_max(nums: list[int], k: int) -> list[int]:
    """Classic monotonic queue solution."""
    if k <= 0:
        raise ValueError("k must be > 0")
    if not nums:
        return []

    q: Deque[int] = deque()  # indices, values decreasing
    res: list[int] = []

    for i, x in enumerate(nums):
        # pop smaller from right
        while q and nums[q[-1]] <= x:
            q.pop()
        q.append(i)

        # pop out-of-window from left
        if q[0] <= i - k:
            q.popleft()

        if i >= k - 1:
            res.append(nums[q[0]])

    return res


def _test_monotonic() -> None:
    assert next_greater_elements([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
    assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


if __name__ == "__main__":
    _test_monotonic()
    print("monotonic_stack_queue.py: OK")
