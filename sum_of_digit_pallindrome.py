def sum_of_digit_is_pallindrome(n):
  return is_pallindrome(sum_of_digit(n));

def sum_of_digit(n):
  sum = 0
  temp = n
  while temp > 0:
    digit = temp % 10;
    sum += digit;
    temp //= 10;
  return sum;

def is_pallindrome(n):
  rev = 0
  temp = n
  while temp > 0:
    digit = temp % 10;
    rev = rev * 10 + digit;
    temp //= 10;
  return "Yes" if rev == n else "No";