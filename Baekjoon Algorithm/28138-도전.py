n, r = map(int, input().split())
m = 1
tot = 0

while n == m:
    m += 1
    if n % m != r:
        print("m", m)