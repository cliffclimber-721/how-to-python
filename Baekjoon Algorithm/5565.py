cash = int(input())
tots = []

for m in range(9):
    m = int(input())
    tots.append(m)

print(cash - sum(tots))