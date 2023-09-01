A, B = [], []
n, m = map(int, input().split())

for _ in range(n):
    r = list(map(int, input().split()))
    A.append(r)

for _ in range(n):
    r = list(map(int, input().split()))
    B.append(r)

for r in range(n):
    for c in range(m):
        print(A[r][c] + B[r][c], end=" ")
    print("")