n, w, h = map(int, input().split())

for _ in range(n):
    l = ((w**2) + (h**2))**0.5
    match = int(input())
    if match <= l:
        print("DA")
    else:
        print("NE")