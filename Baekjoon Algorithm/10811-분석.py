N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]

for _ in range(M):
    b1, b2 = map(int, input().split())
    tmp = basket[b1-1:b2]
    print(basket[b1-1:b2])
    tmp.reverse()
    basket[b1-1:b2] = tmp

for j in range(N):
    print(basket[j], end=' ')