"""Topic: Prefix Sums & Difference Arrays

Use cases
- Range sum queries
- Count subarrays with sum k
- Range updates efficiently (difference arrays)

Key formulas
- prefix[i] = sum(a[0..i-1])
- sum(l..r) = prefix[r+1] - prefix[l]

Pitfalls
- Off-by-one in prefix indexing
- Large sums: Python int is unbounded, but be mindful of performance

My Notes
- 
"""
