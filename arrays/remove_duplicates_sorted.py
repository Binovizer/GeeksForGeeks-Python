def remove_duplicate(arr):
  n = len(arr)
  if n == 0 or n == 1: 
      return n 
  j = 0
  for i in range(n-1): 
      if arr[i] != arr[i+1]: 
          arr[j] = arr[i] 
          j += 1
  arr[j] = arr[n-1] 
  j += 1
  return j