# count compounds

##notes: 
## a counting problem, return up a +1 for valid counts, then return count
## valid count if made the string the whole wayt
## use python startswith()

## its a recursive dp problem by using an index, its reducing the problem space each time
## its efficient because this doesnt do string slicing etc each time 

def count_compounds(compound, elements):
  return _count_compounds(compound, elements, 0, {})

def _count_compounds(compound, elements, idx, memo):
  if idx == len(compound):
    return 1

  if idx in memo:
    return memo[idx]

  count = 0
  for ele in elements:
    if compound.startswith(ele.lower(), idx):
      count += _count_compounds(compound, elements, idx + len(ele), memo)

  memo[idx] = count
  return count