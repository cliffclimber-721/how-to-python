n = int(input())
d = 0
p = 0
rec = [input() for _ in range(n)]

for s in rec:
    if s == "D":
        d += 1
    else:
        p += 1
    
    if abs(d - p) == 2:
        break

print("{}:{}".format(d, p))