def max_index(arr):
    n = len(arr)
    if n <= 1:
        return 0
    maximum = -1
    for i in range(n - 1):
        for j in range(i+1, n):
            if arr[j] >= arr[i]:
                if j - i > maximum:
                    maximum = j - i
    return maximum


def max_index_optimized(arr):
    n = len(arr)
    if n <= 1:
        return 0
    l_min = [0] * n
    r_max = [0] * n
    l_min[0] = arr[0]
    for i in range(1, n):
        l_min[i] = min(arr[i], l_min[i-1])
    r_max[n-1] = arr[n-1]
    for j in range(n-2, -1, -1):
        r_max[j] = max(arr[j], r_max[j + 1])
    i, j = 0, 0
    max_diff = -1
    while i < n and j < n:
        if l_min[i] <= r_max[j]:
            max_diff = max(max_diff, j - i)
            j += 1
        else:
            i += 1
    return max_diff
