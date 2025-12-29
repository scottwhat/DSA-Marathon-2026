"""Topic: Hashing (Maps & Sets)

When to use
- Need O(1) average membership, counting, grouping.

Patterns
- Frequency map (Counter-like)
- Seen set / visited set
- Map from key -> best/first/last index
- Grouping by signature (e.g., sorted string, counts tuple)

Pitfalls
- Custom keys must be hashable/immutable (tuple, frozenset)
- Collisions are handled but can affect performance

Complexities
- Average: insert/lookup O(1)

My Notes
- 
"""
