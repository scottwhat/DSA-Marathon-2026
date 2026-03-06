#notes:
quickest concat grows from previous questions
#use minimum checking logic
# set a min = 'inf'

#then check through the for loop, catch reutnr 1 + for each call
# min check of min_words vs attempt 
def quickest_concat(s, words):
  result = _quickest_concat(s, words, 0, {})
  if result == float('inf'):
    return -1
  else:
    return result

def _quickest_concat(s, words, i, memo):
  if i in memo:
    return memo[i]
  
  if i == len(s):
    return 0
  
  min_words = float('inf')
  for word in words:
    if s.startswith(word, i):
      attempt = 1 + _quickest_concat(s, words, i + len(word), memo)
      min_words = min(attempt, min_words)
  
  memo[i] = min_words
  return min_words

