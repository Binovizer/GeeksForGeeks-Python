def kth_digit(a, b, k):
  rev = 0
  temp = a ** b
  while temp > 0 and k > 0:
    digit = temp % 10;
    temp //= 10;
    k -= 1;
  return digit;