m=5
"""
Creates a 2D cache (list of lists) sized n rows by m columns, initialized to -1.
The list comprehension:
    [[-1] * m for _ in range(n)]
builds n distinct rows. The underscore variable `_` is the loop variable for
`for _ in range(n)` and is used by convention to indicate the loop index is
intentionally unused. It still takes on each value from 0 to n-1, but the code
doesn't reference it; each iteration simply constructs a new row `[-1] * m`.
Using the comprehension ensures each row is a separate list (not multiple
references to the same inner list), avoiding the common pitfall of
`cache = [[-1] * m] * n`.
"""
n=3

make make an array of -1 elements with *m length, for _ in range(n) time
cache = [[-1] * m for x in range(n)]

print(cache )