def angle_between_hour_minute(h, m):
  ha = (h * 30) + (m / 2);
  ma = m * 6
  res = abs(ha - ma)
  anti_res = 360 - res
  return int(res) if res < anti_res else int(anti_res)