def nth_fib_no(n):
  a = 0;
  b = 1;
  for i in range(n-2):
    next_no = (a % 1000000007 + b % 1000000007) % 1000000007
    a = b
    b = next_no
  return next_no

def nth_even_fib_no(n):
  return nth_fib_recursion(n * 3 + 1)

def nth_fib_recursion(n):
  if n <= 1:
    return 0
  if n == 2:
    return 1
  return (nth_fib_recursion(n-1) % 1000000007 + nth_fib_recursion(n-2) % 1000000007 ) % 1000000007