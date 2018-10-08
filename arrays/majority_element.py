def majority_element(arr):
  n = len(arr)
  threshold = n / 2;
  d = {x:arr.count(x) for x in arr}
  elems, counts = list(d.keys()), list(d.values())
  for idx, count in enumerate(counts):
    if count > threshold:
      return elems[idx]
  return -1