# befitting brackets

# hashmap of corresponding brackets, 

#use stack 
def befitting_brackets(string):
  stack = []
  
  brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
  }
  
  for char in string:
    if char in brackets:
      stack.append(brackets[char])
    else:
      if stack and stack[-1] == char:
        stack.pop()
      else:
        return False
      
  return len(stack) == 0