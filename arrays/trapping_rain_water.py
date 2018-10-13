def water(arr):
    n = len(arr)
    l_max = [0] * n
    l_max[0] = arr[0]
    for i in range(1, len(arr)):
        l_max[i] = max(l_max[i-1], arr[i])
    # print(l_max)
    r_max = [0] * n
    r_max[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        r_max[i] = max(r_max[i+1], arr[i])
    # print(r_max)
    ans = 0
    for i in range(n):
        ans += min(l_max[i], r_max[i]) - arr[i]
    return ans
