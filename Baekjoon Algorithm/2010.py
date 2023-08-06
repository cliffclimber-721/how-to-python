import sys
input = sys.stdin.readline

multi = int(input())
tot = 0

for _ in range(multi):
    l = int(input())
    tot += l

print(tot - (multi - 1))