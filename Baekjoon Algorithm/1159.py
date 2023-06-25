n = int(input())

pl_tot = []
re = []

for _ in range(n):
    pl = input()
    pl_tot.append(pl[0])

fn = set(pl_tot) # => {'l', 'j', 'm', 'b', 'k'}
# 이걸 안 써주게 되면 해당개수만큼 알파벳이 출력된다.
# 예를 들어 백준의 첫번째 예시인데, 
# b와 k의 개수가 5개가 넘는데, 얘를 set으로 하지 않으면 bbbbbbkkkkkkk 로 출력된다.
# set으로 해야 값이 하나로 나온다.

for i in fn:
    if pl_tot.count(i) >= 5:
        re.append(i)

if len(re) > 0:
    print(''.join(sorted(re)))
    # sorted = 안에 인덱스 순서대로 나열해준다.
    # ''.join.sorted(re) => join 함수는 해당 인덱스를 구분해주기 위해 쓰는 함수이다.
    # 저 위에처럼 사용된다 그러면 얘의 출력은 
    # sorted(re) 의 값을 ''로 구분지어 출력해달라는 뜻이다.
else:
    print("PREDAJA")