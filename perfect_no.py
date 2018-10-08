from math import sqrt;
def is_perfect_no(n):
  if n == 1:
      return False;
  temp = n;
  sum = 1;
  for i in range(2, n // 2 + 1):
    if n % i == 0:
      sum += i;
  return sum == temp;

def optimised_is_perfect_no(n):
  temp = n;
  f = {1} if n != 1 else set();
  for i in range(2, int(sqrt(n) + 2)):
    if n % i == 0:
      f.update([i, n//i]);
  return temp == sum(f);