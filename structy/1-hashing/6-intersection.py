# intersection

# lesson learnt
def intersection(a, b):

  set_a = set(a)
  ##make 1 set, then do a loop of b
  return [item for item in b if item in set_a]

    ## two loops makes timeout
    ## make 1 a set then use list comprehension to check if items in b are in set a
