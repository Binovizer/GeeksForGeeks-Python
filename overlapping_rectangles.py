def are_overlapping(rect1, rect2):
  if rect1[0] > rect2[2] || rect2[0] > rect1[2]:
    return False
  if rect1[1] < rect2[3] || rect2[1] < rect1[3]:
    return False
  return True