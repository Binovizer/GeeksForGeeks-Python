def product_array(arr):
    prod = 1
    for elem in arr:
        prod *= elem
    for i in range(len(arr)):
        print(prod//arr[i], end=' ')
    print()
