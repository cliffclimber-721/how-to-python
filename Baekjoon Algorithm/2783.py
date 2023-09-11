x, y = map(int, input().split())
v = x*1000 / y
n = int(input())

for _ in range(n):
    xi, yi = map(int, input().split())
    v2 = xi*1000 / yi
    if v > v2:
        v = v2

print(round(v, 2))