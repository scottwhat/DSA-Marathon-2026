# Section Summary — Hashmaps & Sets

- Core concepts: hash table mechanics, average/worst-case complexity, collision handling, load factor.
- Key patterns: frequency counting, two-sum style lookup, sliding-window with counts, grouping by keys, set membership.
- Design/interop: using dicts for memoization, ordered vs unordered maps, when to use set for uniqueness.

Review prompts:
- Explain how a hash map works and why average operations are O(1).
- When is collision a problem; how do common languages handle it?
- Practice patterns: frequency maps, counting distinct, sliding-window frequency problems.
- Design: sketch an LRU cache and explain eviction policy using hashmap+linked list.
- Coding: implement group-anagrams and two-sum using hashing.

## Deep-dive prompts
- Explain average-case vs worst-case behavior of hash tables and why we still treat them as O(1) in interviews.
- When you use a frequency map, what is the key, and what is the update rule?
- For “group by” problems (anagrams), compare key choices: sorted string vs 26-count tuple.
- For sliding windows with counts: how do you maintain “validity” without rescanning the whole window?
- When is a set strictly better than a dict and vice versa?

## Mini quiz (no notes)
1) What’s the difference between “contains duplicate” and “longest consecutive sequence” in terms of hashing usage?
2) Give a canonical-key strategy for anagrams and its time complexity.
3) In Python, what data structure do you use for a multiset / counter?
4) True/False: Hash maps guarantee O(1) worst-case operations.
5) If you need LRU behavior, what 2 structures do you combine and why?

## Operations & gotchas drill
- What are the average-time complexities of: insert, lookup, delete for a hash map? What assumptions are you making?
- Key gotcha: which Python types are hashable/unhashable, and why does mutability matter?
- Collision concept check: what is a collision and why doesn’t it automatically break correctness?
- When using `dict.get(k, 0)`, what bug happens if you forget to write back the increment?
- Frequency-map gotcha: describe the difference between “counting occurrences” and “counting distinct in window” (state maintenance).
- Anagrams key design: compare sorting key vs 26-count tuple (time/space tradeoff).
- Window trick: how do you track “valid window” without rescanning counts each time?
- Set trick: why is `seen.add(x)` in a loop such a common optimization?
- Hashmap trick: when is it useful to map value → index vs value → count?
- Debug drill: if your dict keys look correct but comparisons fail, what should you check (e.g., whitespace, normalization, casing)?

### Quick quiz
1) True/False: Using a tuple of ints as a key is safe in Python.
2) Why can’t you use a list as a dict key?
3) What structure in Python is made for frequency counting?
4) In “two-sum”, why do we store `target - x` or store indices? What is the invariant?
5) What does it mean for a hash table operation to be “amortized” O(1)?
6) True/False: A set preserves insertion order in all languages.
7) When might hashing be worse than sorting in practice?
8) For “longest consecutive sequence”, why does the O(n) set approach work?
