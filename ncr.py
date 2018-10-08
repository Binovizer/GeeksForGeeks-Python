def ncr(n, r):
  if n < r:
      return 0;
  if n == r:
      return 1;
  r = n - r if n - r <= n/2 else r;
  num = 1
  den = 1;
  for i in range(r):
    num *= (n - i);
    den *= (i + 1)
  return (num // den) % (10 ** 9 + 7)