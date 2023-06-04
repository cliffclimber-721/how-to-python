import math as m

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

kor = m.ceil(A / C)
mth = m.ceil(B / D)
mx = max(kor, mth)

print(L - mx)