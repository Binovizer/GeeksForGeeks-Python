def primes_set(upto):
  primes = [True] * (upto + 1)
  primes[0] = False;
  primes[1] = False
  i = 2;
  while i * i <= upto:
    if primes[i]:
      j = 2;
      while i * j <= upto:
        primes[i*j] = False;
        j += 1
    i += 1
  primes_set = []
  for i in range(len(primes)):
    if primes[i]:
      primes_set.append(i)
  return primes_set;
  
def count_three_divisors(n):
    p_set = primes_set(100000)
    count = 0
    for p in p_set:
        if p * p <= n:
            count += 1
        else:
            break;
    return count