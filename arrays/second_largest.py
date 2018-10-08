def second_largest(arr):
  largest = -1
  second_largest = -1
  for elem in arr:
    if elem > largest:
      second_largest = largest
      largest = elem
    elif elem > second_largest:
      second_largest = elem
  return second_largest