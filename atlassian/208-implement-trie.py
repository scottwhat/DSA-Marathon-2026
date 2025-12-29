"""
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/

Commonly asked at Atlassian

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and 
retrieve keys in a dataset of strings. There are various applications of this data structure, 
such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), 
  and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has 
  the prefix prefix, and false otherwise.

Example:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    """
    Time: 
        insert: O(m) where m = length of word
        search: O(m)
        startsWith: O(m)
    Space: O(n * m) where n = number of words, m = avg length
    """
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie"""
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end = True

    def search(self, word: str) -> bool:
        """Returns if the word is in the trie"""
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """Returns if there is any word in the trie that starts with the given prefix"""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True


# Test cases
if __name__ == "__main__":
    trie = Trie()
    
    print("Insert 'apple'")
    trie.insert("apple")
    
    print(f"Search 'apple': {trie.search('apple')}")  # True
    print(f"Search 'app': {trie.search('app')}")      # False
    print(f"StartsWith 'app': {trie.startsWith('app')}")  # True
    
    print("\nInsert 'app'")
    trie.insert("app")
    
    print(f"Search 'app': {trie.search('app')}")      # True
    
    print("\n--- Test 2 ---")
    trie2 = Trie()
    trie2.insert("hello")
    trie2.insert("hell")
    trie2.insert("heaven")
    trie2.insert("goodbye")
    
    print(f"Search 'hell': {trie2.search('hell')}")   # True
    print(f"Search 'hello': {trie2.search('hello')}")  # True
    print(f"Search 'good': {trie2.search('good')}")   # False
    print(f"StartsWith 'he': {trie2.startsWith('he')}")  # True
    print(f"StartsWith 'good': {trie2.startsWith('good')}")  # True
    print(f"StartsWith 'goo': {trie2.startsWith('goo')}")  # True

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

