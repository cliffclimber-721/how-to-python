def quick_sort(num):
    n = len(num)
    if n <= 1:
        return num

    pivot = num[-1] # in quick sort, it needs pivot for the last value
    arr1 = [] # array initialise
    arr2 = []
    for i in range(0, n - 1): # last value is for comparison, so it doesn't includes inside the range
        if num[i] < pivot:
            arr1.append(num[i])
        else:
            arr2.append(num[i])

    return quick_sort(arr1) + [pivot] + quick_sort(arr2)

arrays = [32, 87, 4, 51, 13, 90, 28, 74, 69, 101, 43]
print(quick_sort(arrays))