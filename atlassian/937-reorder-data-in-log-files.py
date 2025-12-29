"""
937. Reorder Data in Log Files
https://leetcode.com/problems/reorder-data-in-log-files/

Commonly asked at Atlassian

You are given an array of logs. Each log is a space-delimited string of words, where the first 
word is the identifier.

There are two types of logs:
- Letter-logs: All words (except the identifier) consist of lowercase English letters.
- Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:
1. The letter-logs come before all digit-logs.
2. The letter-logs are sorted lexicographically by their contents. If their contents are the same, 
   then sort them lexicographically by their identifiers.
3. The digit-logs maintain their relative ordering.

Return the final order of the logs.

Example 1:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Example 2:
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
"""

def reorderLogFiles(logs):
    """
    Time: O(n log n * m) where n = number of logs, m = max length of log
    Space: O(n)
    """
    def get_key(log):
        """
        Return sort key for the log
        - Letter logs: (0, content, identifier)
        - Digit logs: (1,) - maintains original order
        """
        identifier, content = log.split(' ', 1)
        
        if content[0].isalpha():
            # Letter log: sort by content first, then identifier
            return (0, content, identifier)
        else:
            # Digit log: put at end, maintain relative order
            return (1,)
    
    return sorted(logs, key=get_key)


def reorderLogFiles_verbose(logs):
    """
    Alternative: Separate letter and digit logs first
    Time: O(n log n * m)
    Space: O(n)
    """
    letter_logs = []
    digit_logs = []
    
    for log in logs:
        identifier, content = log.split(' ', 1)
        
        if content[0].isalpha():
            letter_logs.append((identifier, content, log))
        else:
            digit_logs.append(log)
    
    # Sort letter logs by content first, then identifier
    letter_logs.sort(key=lambda x: (x[1], x[0]))
    
    # Return sorted letter logs followed by digit logs
    return [log for _, _, log in letter_logs] + digit_logs


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "logs": ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"],
            "expected": ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
        },
        {
            "logs": ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"],
            "expected": ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
        },
        {
            "logs": ["a2 act car", "a1 act car", "di4 4 7 8"],
            "expected": ["a1 act car", "a2 act car", "di4 4 7 8"]
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"=== Test {i} ===")
        logs = test["logs"]
        expected = test["expected"]
        
        result1 = reorderLogFiles(logs.copy())
        result2 = reorderLogFiles_verbose(logs.copy())
        
        print(f"Input: {logs}")
        print(f"Output (key): {result1}")
        print(f"Output (verbose): {result2}")
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

