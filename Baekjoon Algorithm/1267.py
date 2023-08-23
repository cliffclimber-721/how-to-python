n = int(input())
li = list(map(int, input().split()))

y = 0
m = 0

for n in li:
    y += (n // 30 + 1) * 10
    m += (n // 60 + 1) * 15
if y == m:
    print("Y M", m)
elif y > m:
    print("M", m)
else:
    print("Y", y)