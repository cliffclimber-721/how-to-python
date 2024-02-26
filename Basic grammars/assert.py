# assert이 필요한 이유
# 함수 성능을 높이기 위해 특정 값만 받아야하는 상황이 올 수 있는데
# 그럴 때 assert를 사용한다.
lists = [1, 3, 6, 3, 8, 7, 13, 23, 13, 2, 3.14, 2, 3, 7]

def test(t):
    assert type(t) is int, 'not ints'

for i in lists:
    test(i)