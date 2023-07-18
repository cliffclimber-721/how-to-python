N = int(input())

t = list(map(int, input().split()))
tot = sum(t) + (8 * (N-1))

d = tot // 24
h = tot % 24

print(d, h)