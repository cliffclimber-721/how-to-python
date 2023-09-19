import sys

input = sys.stdin.readline

n = int(input())
at = 0
bt = 0

for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        at += 1
    elif a < b:
        bt += 1
    else:
        at += 0
        bt += 0

print(at, bt)