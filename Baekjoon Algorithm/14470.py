A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A < 0:
    print(abs(A) * C + D + abs(B) * E)
elif A > 0:
    print((B - A) * E)
# else 밑에 이건 쓸 필요없음.. 그냥 A가 0일 경우라서
else:
    print(C + (B - 1) * E)