N = int(input())

Y = 0
M = 0
for t in range(N):
    c1, c2, c3 = map(int, input().split())
    Y += (t // 30 + 1) * 10
    M += (t // 60 + 1) * 15

if Y > M:
    print("M", M)
elif Y == M:
    print("Y M", M)
else:
    print("Y", Y)
