def findMax(max): # I use "max" to find the maximum number.
    nums = len(max) # "nums" is a variable to look for the length of "max"
    max_num = max[0] # Remember that inside the first index number is the maximum number.
    for i in range(1, nums):
        if max[i] > max_num: # If "max_num" number is bigger than inside "max[i]"
            max_num = max[i] # The value changes.
    return max_num

num = [17, 100, 94, 5, 32, 44, 87, 29]
print(findMax(num))