def n_fib_no(n):
  fibs = []
  a = 0;
  b = 1;
  fibs.append(a);
  fibs.append(b);
  for i in range(n - 2):
    next_no = a + b
    fibs.append(next_no % 100)
    a = b
    b = next_no
  return fibs

def last_2_digit(n):
  if n <= 0:
    return '00'
  fibs_300 = n_fib_no(300);
  # print(fibs_300)
  return '{:02d}'.format(fibs_300[n % 300])