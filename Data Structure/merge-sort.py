def merge_sort(num):
    n = len(num)
    if n <= 1:
        return num

    mid = n // 2 # this has to be divided into 2 groups, so " mid " is important
    arr1 = merge_sort(num[:mid]) # first to mid
    arr2 = merge_sort(num[mid:]) # mid to last

    result = [] # result initialise
    while arr1 and arr2:
        if arr1[0] < arr2[0]: # compare two values until values aren't inside the array
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))

    while arr1:
        result.append(arr1.pop(0))
    while arr2:
        result.append(arr2.pop(0))
    return result

arrays = [32, 87, 1, 51, 13, 90, 28, 74, 69, 101, 43]
print(merge_sort(arrays))
