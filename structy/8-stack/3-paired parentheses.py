# paired parentheses
#   process a string, check if it has well formed paired_parentheses

#   variation on the standard parenthesis check

#   make a hashmap with open and closed parens, 

#   do a check, if paren, add to stack

#   step it out

#   how do i want to use the stack, add everything on, then add its complement 

#   partners ):()

#  stack = (, (, )
#  count, track parenthesis 
# count how many have been opened, then count down how many were closed 
def paired_parentheses(string):
  #track counts of parens 
  count = 0
  
  for char in string:
    if char == '(':
      count += 1
    elif char == ')':
      if count == 0:
        return False
      count -= 1
      
  return count == 0

