def wave_array(arr):
  arr.sort()
  i = 0
  while i < len(arr) - 1:
    temp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = temp
    i += 2 
  return arr