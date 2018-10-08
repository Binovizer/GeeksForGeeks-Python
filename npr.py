def factorial(n):
  if n <= 1:
    return 1
  return n * factorial(n-1);

def npr(n, r):
  return factorial(n) // factorial(n - r);