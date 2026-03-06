# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:
    """
    A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently
    store and retrieve keys in a dataset of strings.
    """
    
    def __init__(self):
        pass
        
    def insert(self, word: str) -> None:
        """Inserts the string word into the trie."""
        pass
        
    def search(self, word: str) -> bool:
        """Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise."""
        pass
        
    def startsWith(self, prefix: str) -> bool:
        """Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise."""
        pass


# Test cases
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   # Expected: True
    print(trie.search("app"))     # Expected: False
    print(trie.startsWith("app")) # Expected: True
    trie.insert("app")
    print(trie.search("app"))     # Expected: True
