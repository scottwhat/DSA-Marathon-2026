"""
253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/

Commonly asked at Atlassian (Premium)

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Explanation: We need two meeting rooms
Room 1: [0,30]
Room 2: [5,10],[15,20]

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
"""

import heapq

def minMeetingRooms(intervals):
    """
    Time: O(n log n)
    Space: O(n)
    
    Approach: Use min heap to track end times of ongoing meetings
    """
    if not intervals:
        return 0
    
    # Sort meetings by start time
    intervals.sort(key=lambda x: x[0])
    
    # Min heap to track end times
    heap = []
    
    for start, end in intervals:
        # If earliest ending meeting is done, reuse that room
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        
        # Add current meeting's end time
        heapq.heappush(heap, end)
    
    # Size of heap = number of rooms needed
    return len(heap)


def minMeetingRooms_chronological(intervals):
    """
    Alternative approach: Chronological ordering
    Time: O(n log n)
    Space: O(n)
    """
    if not intervals:
        return 0
    
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    
    rooms = 0
    max_rooms = 0
    s, e = 0, 0
    
    while s < len(starts):
        if starts[s] < ends[e]:
            # New meeting starts before earliest ends
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            s += 1
        else:
            # A meeting ended, free up a room
            rooms -= 1
            e += 1
    
    return max_rooms


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[0,30],[5,10],[15,20]], 2),
        ([[7,10],[2,4]], 1),
        ([[1,5],[8,9],[8,9]], 2),
        ([[9,10],[4,9],[4,17]], 2),
    ]
    
    for intervals, expected in test_cases:
        result1 = minMeetingRooms(intervals.copy())
        result2 = minMeetingRooms_chronological(intervals.copy())
        print(f"Input: {intervals}")
        print(f"Output (heap): {result1}")
        print(f"Output (chrono): {result2}")
        print(f"Expected: {expected}")
        print(f"Pass: {result1 == expected and result2 == expected}\n")

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

