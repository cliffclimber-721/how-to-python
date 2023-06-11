p = list(map(int, input().split()))
x, y, r = map(int, input().split())

print(p.index(x) + 1 if x in p else 0)
# index 는 해당 키값이 몇번째 인덱스에 있는지 확인해준다.
# if-in-else 를 연결해서 쓸 수 있는데 이땐 : 를 쓰지 않는다.
# 이걸 쓸 땐 헷갈리면 안된다......