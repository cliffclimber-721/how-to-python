A, B = map(int, input().split())
C = int(input())

if (B+C) < 60:
    print(A, B+C)
elif (B+C) > 60:
    print(A+1, B+C-60)
elif A == 23 or (B+C) > 60:
    print(0, B+C-60)