A, B, C = map(int, input().split())

if (A // B) > (B // C):
    print(int((A // B) * C))
else:
    print(int((B // C) * A))