li = [list(map(int, input().split())) for _ in range(9)]

maxn = 0
maxr, maxc = 0, 0

for r in range(9):
    for c in range(9):
        if maxn <= li[r][c]:
            maxr = r + 1
            maxc = c + 1
            maxn = li[r][c]

print(maxn)
print(maxr, maxc)