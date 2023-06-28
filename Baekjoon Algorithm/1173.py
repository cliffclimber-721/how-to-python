N, m, M, T, R = map(int, input().split())

# 분의 초기값을 위해 min 변수 지정 => 얘를 지정한 이유는 분을 계속 더해줘야하기 때문
# 전체 값을 1씩 더해주면서 찾아줘야하기 때문에 total 변수 지정
min = total = 0
# beat를 설정한 이유는 m은 초기 맥박이기 때문에 따로 저장해줄 값이 필요하다.
beat = m

if m + T > M:
    print(-1)
else:
    while min < N:
        if beat + T <= M:
            beat += T
            min += 1
            total += 1
        else:
            beat -= R
            if beat < m:
                beat = m
            total += 1
    print(total)