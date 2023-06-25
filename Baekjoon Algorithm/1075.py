n = input()
f = int(input())
cn = int(n[:-2] + "00") 
# 맨 뒤 두자리를 유연하게 바꾼다.

while True:
    if (cn % f) == 0:
        print(str(cn)[-2:])
        break
    cn += 1