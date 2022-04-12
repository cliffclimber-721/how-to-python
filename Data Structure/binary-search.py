def binary_search(list, findNum):
    start = 0 # select range
    end = len(list) - 1

    while start <= end: # if range is still in
        mid = (start + end) // 2
        if findNum == list[mid]: # investigated
            return mid
        elif findNum > list[mid]: # if " findNum " is more bigger than inside the array
            start = mid + 1
        else: # if not
            end = mid - 1

    return -1

arr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(binary_search(arr, 36))
print(binary_search(arr, 7))