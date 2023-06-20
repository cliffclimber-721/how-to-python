n, w, h, l = map(int, input().split())

cows = (w // l) * (h // l)
if n > cows:
    print(cows)
else:
    print(n)