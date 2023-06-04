# 어디가 오류인지 모르겠음....

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

kor = A // C
math = B // D
subs = [kor, math]

if A % C == 0 and B % D == 0:
    print(L - max(subs))
else:
    if subs[0] > subs[1]:
        print(L - (subs[0] + 1))
    else:
        print(L - (subs[1] + 1))