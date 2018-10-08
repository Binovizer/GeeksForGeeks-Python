def  triangular_nos(n):
  t_nos = []
  next_no = 0
  for i in range(1, n+1):
    next_no += i
    if next_no <= n:
      t_nos.append(next_no);
    else:
      break;
  return t_nos

def is_triangular_no(n):
  t_nos = triangular_nos(10000000)
  return n in t_nos;