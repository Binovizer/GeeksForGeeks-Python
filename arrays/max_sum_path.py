def max_sum_path(arr1, arr2):
    sum1, sum2 = 0, 0
    n, m = len(arr1), len(arr2)
    i = 0
    while i < n and i < m:
        if arr1[i] == arr2[i]:
            maximum_sum = max(sum1 + arr1[i], sum2 + arr2[i])
            sum1 = maximum_sum
            sum2 = maximum_sum
        else:
            sum1 += arr1[i]
            sum2 += arr2[i]
        i += 1
    while i < n:
        sum1 += arr1[i]
        i += 1
    while i < m:
        sum2 += arr2[i]
        i += 1
    return max(sum1, sum2)

