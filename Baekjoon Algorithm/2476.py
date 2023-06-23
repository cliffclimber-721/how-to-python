dtot = int(input())
mm = 0

for _ in range(dtot):
    d1, d2, d3 = map(int, input().split())
    if d1 == d2 == d3:
        mm = max(mm, 10000 + d1 * 1000)
    elif d1 == d2:
        mm = max(mm, 1000 + d1 * 100)
    elif d2 == d3:
        mm = max(mm, 1000 + d2 * 100)
    elif d1 == d3:
        mm = max(mm, 1000 + d1 * 100)
    else:
        mm = max(mm, max(d1, d2, d3) * 100)

print(mm)