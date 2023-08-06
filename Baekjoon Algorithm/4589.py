n = int(input())

print("Gnomes:")
for _ in range(n):
    g1, g2, g3 = map(int, input().split())
    if g1 < g2 and g2 < g3:
        print("Ordered")
    elif g1 > g2 and g2 > g3:
        print("Ordered")
    else:
        print("Unordered")