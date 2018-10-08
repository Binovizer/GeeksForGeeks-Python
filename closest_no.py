from decimal import Decimal, ROUND_HALF_UP
def closest_number(n, m):
  ans = Decimal(n/m).quantize(0, ROUND_HALF_UP) * m;
  print(0 if ans == -0 else ans)