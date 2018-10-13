def get_length(arr):
    arr = list(set(arr))
    n = len(arr)
    if n == 1:
        return 1
    arr.sort()
    i = 0
    long_seq_len = 0
    while i < n-1:
        start = i
        while i < n - 1 and arr[i] + 1 == arr[i+1]:
            i += 1
        seq_len = i - start + 1
        if seq_len > long_seq_len:
            long_seq_len = seq_len
        i += 1
    return long_seq_len
