M = int(input())

cup = [1, 2, 3]
for _ in range(M):
    X, Y = map(int, input().split())
    c1 = cup.index(X)
    c2 = cup.index(Y)
    cup[c1], cup[c2] = cup[c2], cup[c1]
    # swap 할 때 인덱스 넘버만 기입 잘해주면 된다.
    # python index 함수 활용을 잘해보자,,
print(cup[0])
