def can_be_palindrome(input_str):
    count1 = [0] * 256
    for i in input_str:
        count1[ord(i)] += 1
    if len(input_str) % 2 == 0:
        for i in count1:
            if i % 2 != 0:
                return False
    else:
        count = 0
        for i in count1:
            if i % 2 != 0:
                count += 1
            if count > 1:
                return False
    return True
