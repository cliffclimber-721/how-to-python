a, b = map(int, input().split())

m = (b - a) / 400
wins = 1 / (1 + 10**m)

print(wins)