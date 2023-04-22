star = int(input())

for i in range(1, star):
    print(" " * (star - i) + "*" * (2 * i - 1))

for i in range(star, 0, -1):    
    print(" " * (star - i) + "*" * (2 * i - 1))

# 백준에서 출력시 , 가 아닌 + 을 더 활용해서 출력 진행