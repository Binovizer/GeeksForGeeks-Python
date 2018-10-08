def seq(arr):
  n = len(arr)
  for i in range(n-2):
    for j in range(i+1, n-1):
      for k in range(j+1, n):
        if arr[i] < arr[j] and arr[j] < arr[k]:
          return [arr[i], arr[j], arr[k]]
  return 0