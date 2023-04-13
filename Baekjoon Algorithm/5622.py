dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
word = str(input())
# 나오는 값들마다 더해야하니까 초기값을 설정해준다.
num = 0

# len(word) 인 이유는 해당 문자를 받아왔으면 문자의 개수를 파악한다.
# 파악한 후 배열의 인덱스를 알아낸다.
for w in range(len(word)):
    # 예를 들어, WA를 print(w) 하면 0과 1이 뜨고
    # SKY를 print(w) 하면 0, 1, 2가 뜬다
    for d in dial:
        # 위 dial 리스트에서 이제 아까 word로부터 받아온 문자를 찾는다.
        # "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"
        # 위 문자를 다 받아오고, "" 안에 있는 것을 기준으로 해 출력된다.
        # ABC DEF GHI JKL MNO PQRS TUV WXYZ => 이렇게 나온다.
        if word[w] in d:
        # 그래서 word[w]는 이제 인덱스 넘버가 뜨고 이 넘버가 d 안에 포함되어있다면
        # 해당하는 값을 더해주는 방식이다.
        # dial.index(d) 같은 경우는 예를 들어 WA가 있다면
        # A는 3, W는 10 (맨 앞은 2초가 걸리고, 그 뒤는 1초가 걸린다)
        # 이렇게 더하는 방식이다.
        # 3을 더하는 이유는 ABC는 배열 인덱스 상으로는 0이지만 위치는 2번째기 때문에
        # 3을 더해주는 것이다.
        # 그 뒤 숫자들 또한 3을 더해줘야 계산이 맞다.
            num += dial.index(d) + 3

print(num)