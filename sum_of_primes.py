def sum_of_primes(upto):
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
  return sum(primes_set);