def find_pairs(arr, k):
    ans = []
    n = len(arr)
    for i in range(n-1):
        remaining = k - arr[i]
        if remaining <= arr[i]:
            break
        # print('finding {}'.format(remaining))
        start = i
        end = n-1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == remaining:
                pair = (arr[i], remaining)
                ans.append(pair)
                break
            elif arr[mid] < remaining:
                start = mid + 1
            elif arr[mid] > remaining:
                end = mid - 1
    if len(ans) == 0:
        print(-1)
    else:
        print(ans)
