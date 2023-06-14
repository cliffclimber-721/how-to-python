import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

e1 = A / B * C
e2 = A * B / C

if e1 > e2:
    print(int(e1))
else:
    print(int(e2))