remains = []

for i in range(10):
    i = int(input())
    remains.append(i % 42)

remains = set(remains)
print(len(remains))