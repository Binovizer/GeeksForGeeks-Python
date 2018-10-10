def print_duplicates(arr):
    uniques = set()
    for elem in arr:
        if elem in uniques:
            print(elem, end=' ')
        else:
            uniques.add(elem)
