import sys
input = sys.stdin.readline
# 위 sys 쓰는 이유는 시간 초과를 막기 위해서

for _ in range(3):
    N = int(input())
    tot = 0
    for i in range(N):
        tot += int(input())
    if tot == 0:
        print("0")
    elif tot > 0:
        print("+")
    else:
        print("-")