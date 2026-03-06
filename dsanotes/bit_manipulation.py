"""Topic: Bit Manipulation

Basics
- &, |, ^, ~, <<, >>

Common tricks
- Check bit: (x >> k) & 1
- Set bit: x | (1 << k)
- Clear bit: x & ~(1 << k)
- Lowest set bit: x & -x

Pitfalls
- Python ints are unbounded (no overflow), but shifts can grow large

My Notes
- 
"""
