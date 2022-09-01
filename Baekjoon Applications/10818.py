n = int(input())
nums = list(map(int, input().split()))

if n != len(nums):
    print("Re-Enter!")
elif n == len(nums):
    max = nums[0]
    min = nums[0]
    for i in nums[1:]:
        if i > max:
            max = i
        elif i < min:
            min = i
    
    print(min, max)
