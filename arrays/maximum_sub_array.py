def max_sub_array(arr):
  maxima = -9897876567987
  local_maxima = -9897876567987
  start_maxima = start_local_maxima = end_maxima = 0
  for i in range(len(arr)):
    local_maxima += arr[i] 
    if local_maxima >= maxima:
      maxima = local_maxima
      start_maxima = start_local_maxima
      end_maxima = i
    if local_maxima < 0 or arr[i] < 0: # Second condition for non negative subarray
      local_maxima = 0
      start_local_maxima = i + 1
  return arr[start_maxima: end_maxima+1]

def max_sub_array_sum(arr):
  max_so_far = arr[0]
  curr_max = arr[0]
  for i in range(1, len(arr)):
    curr_max = max(arr[i], arr[i] + curr_max)
    max_so_far = max(curr_max, max_so_far)
  return max_so_far