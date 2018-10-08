def is_armstrong(n):
  digits = [int(digit) for digit in list(n)]
  sum = 0
  for digit in digits:
    sum += digit ** 3;
  return "Yes" if sum == int(n) else "No"

def is_armstrong_number(n):
  sum = 0
  temp = n
  while temp > 0:
    digit = temp % 10;
    sum += digit ** 3;
    temp //= 10;
  return "Yes" if sum == n else "No"