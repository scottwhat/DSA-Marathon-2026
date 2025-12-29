# Section Summary — Tries (Neetcode)

- Focus: prefix trees for string datasets, space-vs-time tradeoffs.

Review prompts:
- When use a trie vs hash map for prefix operations?
- Practice: implement basic trie and word search II approach outline.

## Deep-dive prompts
- Explain trie node structure (children + end-of-word) and how insert/search works.
- Compare trie vs hash set for prefix queries.
- For word search II, why is trie + DFS better than checking each word separately?

## Mini quiz (no notes)
1) True/False: Trie search is O(length of word).
2) What does the end-of-word marker prevent?
3) Name two memory optimizations for tries.
4) In word search II, what is the pruning condition during DFS?

## Operations & gotchas drill
- Operations: insert/search/startsWith — what is their time in terms of word length?
- Memory gotcha: why tries can be memory heavy; what compressions exist (map children, radix tree).
- Word search: what’s the pruning condition using trie?
- Duplicate results: how do you avoid returning the same word multiple times?
- Implementation gotcha: when do you mark end-of-word and how do you store full words efficiently?

### Quick quiz
1) True/False: Trie operations depend on number of stored words.
2) What does an end-of-word marker enable?
3) Why is trie good for prefix queries?
4) In DFS + trie, what makes a branch dead early?
5) Name one alternative structure for prefix search.
