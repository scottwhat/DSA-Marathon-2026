# subsets

#notes 
# recursive approach include or exclude as moving through
# algomap uses backtracking approach

 a,b,c

A:   a
[] [a]

take b or exlcude b
B:  [], [b]   [a], [a,b]

C: take c or exclude c
[], [c]  , [b], [b,c]  [a],[ac] [a,b], [a,b,c]



def subsets(elements):
 
 if not elements:
  return [[]]
 
 first=elements[0]d
 remaining=elements[1:]
#what two choices / parts are we building, 
#each recursive call passes 
 subsets_without_first = subsets(remaining)

 subsets_with_first = []
 for el in elements:
  subsets_with_first