"""python_loops_iterators_dsa.py

A compact, copy-pasteable reference of Python loop + iterator syntax
commonly used in DSA.

This file is intentionally example-heavy and dependency-light.
"""

from __future__ import annotations

from collections import deque
from itertools import (
    accumulate,
    chain,
    combinations,
    combinations_with_replacement,
    count,
    cycle,
    groupby,
    islice,
    permutations,
    product,
    repeat,
)
from typing import Iterable, Iterator, List, Sequence, Tuple


# ============================================================
# 1) Basic loops
# ============================================================

def loops_for_basics(nums: List[int]) -> None:
    """Core `for` loop variants."""

    # Iterate values
    for x in nums:
        _ = x

    # Iterate indexes
    for i in range(len(nums)):
        _ = nums[i]

    # Index + value (preferred)
    for i, x in enumerate(nums):
        _ = (i, x)

    # Start index at 1
    for i, x in enumerate(nums, start=1):
        _ = (i, x)

    # Reverse iteration (values)
    for x in reversed(nums):
        _ = x

    # Reverse iteration (index + value)
    for i in range(len(nums) - 1, -1, -1):
        _ = (i, nums[i])

    # Custom steps
    for i in range(0, len(nums), 2):
        _ = nums[i]

    # Loop with else: runs if NOT broken
    for x in nums:
        if x == -1:
            break
    else:
        # no break happened
        pass


def loops_while_basics(nums: List[int]) -> None:
    """Core `while` loop variants."""

    # Standard index-based while
    i = 0
    while i < len(nums):
        _ = nums[i]
        i += 1

    # Infinite loop with explicit break
    while True:
        if not nums:
            break
        nums.pop()

    # While-else: else runs if loop ended naturally (no break)
    i = 0
    while i < 3:
        i += 1
        if i == 10:
            break
    else:
        # no break happened
        pass


# ============================================================
# 2) Common DSA loop patterns
# ============================================================

def two_pointers_basic(arr: Sequence[int], target: int) -> Tuple[int, int] | None:
    """Example: sorted array 2-sum using two pointers."""
    l, r = 0, len(arr) - 1
    while l < r:
        s = arr[l] + arr[r]
        if s == target:
            return l, r
        if s < target:
            l += 1
        else:
            r -= 1
    return None


def sliding_window_fixed_k(arr: Sequence[int], k: int) -> int:
    """Example: max sum of any window of size k."""
    if k <= 0 or k > len(arr):
        raise ValueError("k must be in [1, len(arr)]")

    window_sum = sum(arr[:k])
    best = window_sum
    for r in range(k, len(arr)):
        window_sum += arr[r] - arr[r - k]
        best = max(best, window_sum)
    return best


def sliding_window_variable(arr: Sequence[int], target: int) -> int:
    """Example: smallest length subarray with sum >= target (positive ints)."""
    best = float("inf")
    l = 0
    window_sum = 0

    for r, x in enumerate(arr):
        window_sum += x
        while window_sum >= target:
            best = min(best, r - l + 1)
            window_sum -= arr[l]
            l += 1

    return 0 if best == float("inf") else int(best)


def bfs_queue_levels(start: int, adj: List[List[int]]) -> List[List[int]]:
    """Example BFS that iterates level-by-level."""
    q = deque([start])
    seen = {start}
    levels: List[List[int]] = []

    while q:
        level_size = len(q)
        level: List[int] = []
        for _ in range(level_size):
            node = q.popleft()
            level.append(node)
            for nei in adj[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
        levels.append(level)

    return levels


# ============================================================
# 3) Iterators: syntax + protocol
# ============================================================

def iterator_protocol_demo(nums: List[int]) -> List[int]:
    """Shows iter()/next() and StopIteration handling."""
    it = iter(nums)  # Iterator
    out: List[int] = []

    while True:
        try:
            out.append(next(it))
        except StopIteration:
            break

    return out


def iter_with_sentinel(file_obj) -> int:
    """Read chunks until empty using `iter(callable, sentinel)`.

    Example usage:
        with open('data.bin', 'rb') as f:
            total = iter_with_sentinel(f)
    """
    total = 0
    for chunk in iter(lambda: file_obj.read(4096), b""):
        total += len(chunk)
    return total


# ============================================================
# 4) Enumerate / Zip (pairing iterables)
# ============================================================

def zip_patterns(a: Sequence[int], b: Sequence[int]) -> None:
    # Pair values (stops at shortest)
    for x, y in zip(a, b):
        _ = (x, y)

    # Pair with index
    for i, (x, y) in enumerate(zip(a, b)):
        _ = (i, x, y)

    # Zip 3+ iterables
    c = list(range(min(len(a), len(b))))
    for x, y, z in zip(a, b, c):
        _ = (x, y, z)


# ============================================================
# 5) List/Dict/Set comprehensions + generator expressions
# ============================================================

def comprehension_patterns(nums: Sequence[int]) -> Tuple[List[int], List[int], List[Tuple[int, int]]]:
    squares = [x * x for x in nums]

    # With condition
    evens = [x for x in nums if x % 2 == 0]

    # Double loop
    pairs = [(i, j) for i in range(3) for j in range(2)]

    # Generator expression (lazy)
    gen = (x * x for x in nums)
    _ = next(gen, None)

    return squares, evens, pairs


# ============================================================
# 6) Useful built-in iterators
# ============================================================

def builtin_iterators(nums: Sequence[int]) -> None:
    # range is an iterable (memory efficient)
    for _ in range(5):
        pass

    # reversed(seq) returns an iterator
    for _ in reversed(nums):
        pass

    # sorted() returns a list; iter(sorted(...)) is an iterator
    for _ in iter(sorted(nums)):
        pass

    # map/filter return iterators
    for _ in map(str, nums):
        pass

    for _ in filter(lambda x: x % 2 == 0, nums):
        pass


# ============================================================
# 7) itertools patterns that show up in DSA
# ============================================================

def itertools_core_examples(nums: Sequence[int]) -> None:
    # Combinatorics
    for comb in combinations(nums, 2):
        _ = comb

    for comb in combinations_with_replacement(nums, 2):
        _ = comb

    for perm in permutations(nums, 2):
        _ = perm

    # Cartesian product
    for tup in product([0, 1], repeat=3):
        _ = tup

    # Accumulate (prefix sums)
    prefix = list(accumulate(nums))
    _ = prefix

    # chain: flatten / concatenate iterables lazily
    flattened = list(chain([1, 2], [3], [4, 5]))
    _ = flattened

    # islice: take a window of an iterator (lazy)
    first_three = list(islice(iter(nums), 3))
    _ = first_three

    # groupby: groups consecutive equal keys (sort first if needed)
    s = "aaabbbcca"
    groups = [(k, ''.join(g)) for k, g in groupby(s)]
    _ = groups


# ============================================================
# 8) Sentinel patterns + next(..., default)
# ============================================================

def safe_next_example(nums: Sequence[int]) -> int:
    it = iter(nums)
    first = next(it, -1)  # default if empty
    return first


# ============================================================
# 9) Loop control: break/continue/pass (quick reference)
# ============================================================

def loop_control_examples(nums: Sequence[int]) -> int:
    total = 0
    for x in nums:
        if x < 0:
            continue
        if x == 0:
            break
        total += x
    return total


if __name__ == "__main__":
    # Tiny smoke run (doesn't print much; just ensures syntax is valid).
    assert iterator_protocol_demo([1, 2, 3]) == [1, 2, 3]
    assert two_pointers_basic([1, 2, 4, 7, 11], 9) == (1, 3)
    assert sliding_window_fixed_k([1, 2, 3, 4], 2) == 7
    assert safe_next_example([]) == -1
