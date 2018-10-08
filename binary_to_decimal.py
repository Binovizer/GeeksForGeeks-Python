def bin_to_dec(bin):
  bin_str = reversed(list(bin))
  num = 0;
  for idx, x in enumerate(bin_str):
    num += int(x) * (2 ** idx);
  return num;  