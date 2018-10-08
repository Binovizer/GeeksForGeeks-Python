def is_jumping_no(num):
  digits = [int(x) for x in str(num)]
  for i in range(len(digits) - 1):
    if abs(digits[i] - digits[i+1]) != 1:
      return "No"
  return "Yes"

def generate_jumping_numbers()