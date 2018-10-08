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
    pass
