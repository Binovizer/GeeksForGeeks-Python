def searchEle(a, x):
  return x in a;

def insertEle(a, y, yi):
  before_len = len(a)
  a.insert(yi, y);
  after_len = len(a)
  return True if after_len - before_len == 1 else False

def deleteEle(a, z):
  if z not in a:
    return True
  before_len = len(a)
  a.remove(z);
  after_len = len(a)
  return True if before_len - after_len == 1 else False