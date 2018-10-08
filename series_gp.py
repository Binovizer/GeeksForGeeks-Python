from math import floor
def gp(first, second, n):
  r = second / first;
  return floor(first * (r ** (n-1)));