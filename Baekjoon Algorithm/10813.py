# 먼저 배열값을 서로 교환하거나 바꿔준다 => 이 뜻은 임의의 공간을 하나 생성해야한다는 뜻이다.
N, M = map(int, input().split())
# 아래와 같이 배열선언해주면 N의 값이 5일 땐 [1, 2, 3, 4, 5]가 보인다.
basket = [i for i in range(1, N+1)]
tmp = 0

for _ in range(M):
    i, j = map(int, input().split())
    tmp = basket[i-1]
    # tmp 는 임의의 변수다. 변수값을 받기 위한 임의의 변수.
    # i에 1을 받아오면 basket의 인덱스는 0이 된다. 
    # 그렇게 되면 basket의 수는 1이 된다. 그럼 tmp 값은 1 
    basket[i-1] = basket[j-1]
    # j의 값을 2를 받아오게 되면, basket의 1번째 인덱스의 값이 1이 된다.
    # 그래서 처음 받아온 1과 2의 값을 swap
    basket[j-1] = tmp
    # 첫번째 값으로 받아온 건 tmp에 넣는다. 개념을 다시 살펴보자.

for b in basket:
    print(b, end=' ')