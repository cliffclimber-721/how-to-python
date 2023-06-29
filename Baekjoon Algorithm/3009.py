x = []
y = []

for _ in range(3):
    c1, c2 = map(int, input().split())
    x.append(c1)
    y.append(c2)

for i in range(3):
    if x.count(x[i]) == 1:
        cf1 = x[i]
    if y.count(y[i]) == 1:
        cf2 = y[i]

print(cf1, cf2)