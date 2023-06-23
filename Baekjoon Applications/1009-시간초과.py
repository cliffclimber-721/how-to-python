import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    data_total = (a**b) % 10
    print(data_total)