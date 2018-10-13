def find_diff(arr, no_of_students):
    n = len(arr)
    arr.sort()
    min_diff = 898988989
    for i in range(n-no_of_students+1):
        diff = arr[i+no_of_students-1] - arr[i]
        if diff < min_diff:
            # print('{} {}'.format(i, i+no_of_students))
            min_diff = diff
    return min_diff
