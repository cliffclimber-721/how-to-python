a, b, c, d = map(int, input().split())
deliv = list(map(int, input().split()))

for i in deliv:
    dogs = 0
    # list로 값을 정해준 이유는 배달기사가 3명이다 보니까 이걸 돌아가면서 검사한다.
    if 0 < i % (a+b) <= a:
        dogs+=1
    if 0 < i % (c+d) <= c:
        dogs+=1
    print(dogs)