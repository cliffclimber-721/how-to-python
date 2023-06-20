pt = 0
maxP = []

for i in range(4):
    p1, p2 = map(int, input().split())
    pt += p2 - p1
    maxP.append(pt)

print(max(maxP))