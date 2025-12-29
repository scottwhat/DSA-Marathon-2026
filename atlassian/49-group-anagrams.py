"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Commonly asked at Atlassian

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

from collections import defaultdict

def groupAnagrams(strs):
    """
    Time: O(n * k log k) where n = len(strs), k = max length of a string
    Space: O(n * k)
    
    Approach: Use sorted string as key
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Sort string to get canonical form
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())


def groupAnagrams_counting(strs):
    """
    Time: O(n * k) where n = len(strs), k = max length of a string
    Space: O(n * k)
    
    Approach: Use character count as key (faster than sorting)
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Count characters (a-z only)
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        # Use tuple of counts as key (lists aren't hashable)
        key = tuple(count)
        groups[key].append(s)
    
    return list(groups.values())


# Test cases
if __name__ == "__main__":
    test_cases = [
        (["eat","tea","tan","ate","nat","bat"], 
         [["bat"],["nat","tan"],["ate","eat","tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]
    
    for strs, expected in test_cases:
        result1 = groupAnagrams(strs.copy())
        result2 = groupAnagrams_counting(strs.copy())
        print(f"Input: {strs}")
        print(f"Output (sorted): {result1}")
        print(f"Output (counting): {result2}")
        print(f"Expected: {expected}")
        # Sort for comparison since order doesn't matter
        result1_sorted = [sorted(group) for group in sorted(result1)]
        expected_sorted = [sorted(group) for group in sorted(expected)]
        print(f"Pass: {result1_sorted == expected_sorted}\n")

# DSA Approach (Concise Prep Checklist)
# 1. Repeat the question
# - Restate problem in one sentence (inputs -> transformation -> output)
# - Confirm input types, indexing (0 vs 1), single vs multiple test cases
# - Ask edge cases: empty, single element, duplicates, negatives, overflow
# - Confirm allowed operations: modify input, sort, extra memory, recursion limits
# - Clarify constraints: max/min n, value ranges, time/memory limits, target Big-O
# - Confirm output format, ordering, stability, tie-breakers, no-solution behavior
# - Ask for 1 normal + 1 tricky example with expected output
# - Confirm environment expectations: libraries, full I/O vs function only, tests required

# 2. Clarifying questions
# - Inputs: type, size, range, sorted?, mutable?
# - Outputs: format, order, duplicates allowed?
# - Constraints: n, value bounds, performance target
# - Sorting: allowed? stability required?
# - Memory: fits in memory or streaming?
# - Special cases: empty, all same, extreme values, cycles (if applicable)

# 3. Work through an example
# - Use small sample input
# - Step through logic manually
# - Track pointers/stack/queue/map state
# - Verify expected output and edge behavior

# 4. Brainstorm solutions
# - Identify pattern: hash, two pointers, sliding window, stack, heap, BFS/DFS, DP, greedy
# - Start with brute force and its Big-O
# - Propose optimal approach and tradeoffs
# - Match data structure to need (lookup, ordering, top-k, dependencies)

# 5. Step out the solution
# - Choose approach + data structures
# - Write steps in plain logic/pseudocode
# - Define loop invariants
# - Dry-run on example
# - State time and space complexity

# 6. Convert to code
# - Translate steps directly to code
# - Comment intent and invariants
# - Handle edge cases early
# - Re-run example and edge cases mentally
# 7. Verify and explain
# - Restate final Big-O
# - Explain correctness briefly
# - Mention alternative approaches if asked

