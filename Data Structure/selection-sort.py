def findMinIdx(num):
    n = len(num)
    min_idx = 0
    for i in range(1, n):
        if num[i] < num[min_idx]:
            min_idx = i
    return min_idx

def selection_sort(n):
    result = [] # make a new list to store values
    while n: # while inside " n "
        min_idx = findMinIdx(n) # find minimum value
        value = n.pop(min_idx) # and put it in " value "
        result.append(value) # and append it
    return result

arr = [3, 7, 10, 2, 6]
print(selection_sort(arr))