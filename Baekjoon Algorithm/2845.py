L, P = map(int, input().split())
R = list(map(int, input().split()))

to = L * P
print(R[0] - to, R[1] - to, R[2] - to, R[3] - to, R[4] - to)