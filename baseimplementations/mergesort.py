
# def merge_sort(nums):
#   if len(nums) <= 1:
#     return nums  
#   mid_idx = len(nums) // 2
#   left_sorted = merge_sort(nums[:mid_idx])
#   right_sorted = merge_sort(nums[mid_idx:])  
#   return merge(left_sorted, right_sorted)

# def merge(list_1, list_2):
#   list_1 = deque(list_1)
#   list_2 = deque(list_2)
  
#   merged = []
#   while list_1 and list_2:
#     if list_1[0] < list_2[0]:
#       merged.append(list_1.popleft())
#     else:
#       merged.append(list_2.popleft())
#   merged += list_1
#   merged += list_2
#   return merged


#what is merge sort

def merge_sort(nums):
    # base implementation
    if nums <= 1:
        return nums
    
    #split them at the middle
    mid_index = len(nums) // 2
    left_nums = merge_sort(nums[:mid_index])
    right_nums = merge_sort(nums{mid_index:})

def merge():
