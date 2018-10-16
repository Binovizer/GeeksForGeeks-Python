def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    count1 = [0] * 256
    for i in str1:
        count1[ord(i)] += 1
    count2 = [0] * 256
    for i in str2:
        count2[ord(i)] += 1
    for i in range(len(count1)):
        if count1[i] != count2[i]:
            return False
    return True
