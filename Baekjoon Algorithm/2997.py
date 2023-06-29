nums = list(map(int, input().split()))

nums.sort()

d = min(nums[2] - nums[1], nums[1] - nums[0])

for i in range(len(nums)):
    tmp = nums[i]
    if tmp + d not in nums:
        print(tmp + d)
        break
