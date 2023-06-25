tot = []

for _ in range(7):
    n = int(input())

    if n % 2 == 1:
        tot.append(n)

if tot:
    print(sum(tot))
    print(min(tot))
else:
    print("-1")