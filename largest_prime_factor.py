from math import sqrt
def largest_prime_factor(n):
  while n % 2 == 0:
    n //= 2;
  if n == 1:
    return 2;
  i = 3;
  while i <= sqrt(n):
    while n % i == 0:
      n //= i;
    if n == 1:
      return i;
    i += 2;
  return n;
