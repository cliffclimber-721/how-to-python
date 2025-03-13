nums = list(map(int, input().split()))
abc = input()
nums = sorted(nums)

for i in abc:
    if i == "A":
        print(nums[0], end=' ')
    elif i == "B":
        print(nums[1], end=' ')
    elif i == "C":
        print(nums[2], end=' ')