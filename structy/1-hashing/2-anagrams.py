# anagrams

## Lessons learnt: check if length of both strings is the same at start
## use options with earlier exits to avoid unneccessary computation
## fewer operations and less memory utilised 

# DSA Approach (Concise Prep Checklist)
##
# 1. Repeat the question - take in two strings as arguements, returns a boolean indicating wether they are anangrams
# what is an anangram? - a word formed by the same letters but in different order 
# - Restate problem in one sentence (inputs -> transformation -> output) take in string array, return boolean if anagagram
# - Confirm input types, indexing (0 vs 1), single vs multiple test cases
# - Ask edge cases: empty, single element, duplicates, negatives, overflow
# - Confirm allowed operations: modify input, sort, extra memory, recursion limits
# - Clarify constraints: max/min n, value ranges, time/memory limits, target Big-O 
# largest string input? 
# if a string length 1 is 1?
# same elements,
# - Confirm output format, ordering, stability, tie-breakers, no-solution behavior
# output booleans only 
# - Ask for 1 normal + 1 tricky example with expected output
## 
# - Confirm environment expectations: libraries, full I/O vs function only, tests required
## none for now 

# 2. Clarifying questions
# - Inputs: type, size, range, sorted?, mutable?
# - Outputs: format, order, duplicates allowed?
# - Constraints: n, value bounds, performance target
# - Sorting: allowed? stability required?
# - Memory: fits in memory or streaming?
# - Special cases: empty, all same, extreme values, cycles (if applicable)

# 3. Work through an example
# take input strings s1 and s2 - hash them 
# becareful, havent yet decided a data structure so may change how you think and approach the problem 
# check s1[0] s2[0] 

# - Use small sample input
# - Step through logic manually
# - Track pointers/stack/queue/map state
# - Verify expected output and edge behavior

# 4. Brainstorm solutions
# - Identify pattern: hash, two pointers, sliding window, stack, heap, BFS/DFS, DP, greedy
## use hashmap to store counts of letters in s1, then decrement counts for letters in s2
## get all down to if all values in hashmap are 0 at end
## other approach - sort both strings and compare

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

