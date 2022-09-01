list = []
for i in range(9):
    list.append(int(input()))

print(max(list))
print(max.index(max(list))+1)