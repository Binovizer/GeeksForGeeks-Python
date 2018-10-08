def rotate(arr, noe):
  length = len(arr)
  new_arr = []
  for i in range(length):
    new_idx = (length + i - noe) % length
    new_arr.insert(new_idx, arr[i])
  return new_arr

def print_array(arr):
  for elem in arr:
    print(elem, end=' ')
  print()