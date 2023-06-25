t = int(input())

for _ in range(t):
    b = input()
    candy = int(input()) # 사탕을 준 아이들의 수, 즉 사탕을 똑같이 배분해야할 아이들의 수

    tot = 0

    for i in range(candy):
        tot += int(input())
    
    if tot % candy == 0:
        print("YES")
    else:
        print("NO")