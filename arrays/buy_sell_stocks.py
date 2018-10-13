def buy_sell_stocks(arr):
    ans = []
    pre = arr[0]
    for i in range(1, len(arr)):
        start = i
        while i < len(arr) and arr[i] > pre:
            pre = arr[i]
            i += 1
        if start == i:
            continue
        else:
            ans.append((start - 1, i - 1))
    print(ans)
