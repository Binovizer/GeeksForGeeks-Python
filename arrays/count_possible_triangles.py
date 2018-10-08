def count(arr):
  arr = list(set(arr))
  print(arr)
  n = len(arr)
  if n < 3:
    return 0
  count = 0
  for i in range(n-2):
    for j in range(i+1, n-1):
      for k in range(j+1, n):
        if arr[i] + arr[j] > arr[k]:
          # print(arr[i], arr[j], arr[k])
          count += 1
  return count