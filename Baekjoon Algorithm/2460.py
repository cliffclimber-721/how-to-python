pt = 0
psg = []

for _ in range(10):
    p1, p2 = map(int, input().split())
    pt += p2 - p1
    psg.append(pt)
    
print(max(psg))