A, B = map(int, input().split())
C = int(input())

A += int(C / 60)
B += int(C % 60)

if B >= 60:
    A += 1
    B -= 60
if A >= 24:
    A -= 24

print(A, B)