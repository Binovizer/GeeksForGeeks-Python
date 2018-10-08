def trailing_zeros(n):
  count = 0
  power = 5
  while power <= n:
    count += (n // power)
    power *= 5
  return count