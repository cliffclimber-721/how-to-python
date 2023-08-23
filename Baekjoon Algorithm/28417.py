import sys
input = sys.stdin.readline

n = int(input())
res = 0

for _ in range(n):
    score = list(map(int, input().split()))
    r = max(score[0:2])
    t = sorted(score[2:])[3:]
    tot = sum(t) + int(r)
    res = max(res, tot)
    
print(res)