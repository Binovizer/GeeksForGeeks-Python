def leaders(arr):
  ans = []
  n = len(arr)
  for i in range(n-1):
    j = 0
    for j in range(i+1, n):
        flag = True
        if arr[i] < arr[j]:
            flag = False
            break
    if flag:
      ans.append(arr[i])
  ans.append(arr[n-1])
  return ans

def leaders_optimised(arr):
  ans = []
  n = len(arr)
  maximus = -1
  for i in range(n-1, -1, -1):
    if arr[i] >= maximus:
      ans.append(arr[i])
      maximus = arr[i]
  ans.reverse()
  return ans