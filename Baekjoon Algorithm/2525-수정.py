A, B = map(int, input().split())
C = int(input())

if (B + C) < 60:
    print(A, B+C)
elif (B + C) > 60:
    time_plus = A + int((B + C) / 60)
    time_rest = int(B + C) % 60
    print(time_plus, time_rest)
