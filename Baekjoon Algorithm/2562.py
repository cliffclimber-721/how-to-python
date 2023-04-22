num=[]

for _ in range(1, 10):
    i = int(input())
    num.append(i)

findMax = max(num)
print(findMax)
print(num.index(findMax)+1)