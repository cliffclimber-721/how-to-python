dtot = []
N = int(input())

for _ in range(N):
    d1, d2, d3 = map(int, input().split())
    if d1 == d2 == d3:
        ft = 10000 + 1000 * d1
    elif d1 == d2 or d1 == d3:
        st = 1000 + 100 * d1
    elif d2 == d3:
        tt = 1000 + 100 * d2
    else:
        dtot.append(d1);dtot.append(d2);dtot.append(d3)
        fot = max(dtot) * 100

print(max(ft, st, tt, fot))