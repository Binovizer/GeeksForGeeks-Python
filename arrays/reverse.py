def reverse(arr):
  arr.reverse()
  return arr

def custom_rev(arr):
  length = len(arr)
  i = 0
  while i < length/2:
    temp = arr[i];
    arr[i] = arr[length - i - 1] 
    arr[length - i - 1] = temp
    i += 1
  return arr