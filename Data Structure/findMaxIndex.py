def findMaxIndex(idx):
    nums = len(idx) # "nums" is a variable for the length
    max_index = 0

    for i in range(1, nums):
        if idx[i] > idx[max_index]:
            max_index = i
    return max_index

arr = [2, 37, 14, 21, 45, 20, 69, 77]
print(findMaxIndex(arr))