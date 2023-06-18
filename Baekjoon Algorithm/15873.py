# 뭔 소리야..
n = input()

# 왜 아래가 저게..
if len(n) == 4:
    print(20)
elif len(n) == 2:
    print(int(n[0]) + int(n[1]))
else:
    if int(n[-1]) == 0:
        print(int(n[0]) + 10)
    else:
        print(int(n[-1]) + 10)