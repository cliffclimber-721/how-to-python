num1 = int(input())
num2 = input()

for n in reversed(range(3)):
    nums = list(str(num2))[n]
    print(num1 * int(nums))
    
print(num1 * int(num2))