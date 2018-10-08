def min_distance(arr, x, y):
  if x not in arr or y not in arr:
    return -1
  indicesX = [idx for idx, elem in enumerate(arr) if elem == x]
  indicesY  = [idx for idx, elem in enumerate(arr) if elem == y]
  min = 9090900909090
  for indexX in indicesX:
    for indexY in indicesY:
      dist = abs(indexX - indexY)
      if min > dist:
        min = dist
  return min