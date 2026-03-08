def permutations(items):
  if not items:
    return [[]]
  
  first = items[0]
  remaining = items[1:]
  perms = permutations(remaining)
  result = []
  for perm in perms:
    for i in range(len(perm) + 1):
      result.append([*perm[:i], first, *perm[i:]])
    
  return result

## builds up the whole time until the final results array is returned 
print(permutations(["a","b","c"]))

# ── Alternative: backtracking with explicit helper ────────

# More intuitive read: "at each step, pick one unused item,
# add it to the current path, recurse, then undo the pick."




##### Backtracking + recursive approach witha  used set. add and pop the used 
# def permutations(items):
#     results = []
#     _helper(items, [], set(), results)
#     return results

# def _helper(items, path, used, results):
#     if len(path) == len(items):
#         results.append(path[:])   # snapshot of complete permutation
#         return

#     for i, item in enumerate(items):
#         if i in used:
#             continue
#         used.add(i)               # choose
#         path.append(item)
#         _helper(items, path, used, results)
#         path.pop()                # unchoose
#         used.remove(i)