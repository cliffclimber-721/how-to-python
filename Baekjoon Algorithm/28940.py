n = int(input())
li = []

for _ in range(n):
    i, j = map(int, input().split())
    res = i * j
    li.append(res)

print(max(li))