s1, s2, s3 = map(int, input().split())
tot = []

for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            res = i + j + k
            tot.append(res)

print(max(set(tot), key=tot.count))
# max 함수 쓰는 방법이
# tot에 대해 집합을 만들어서 제일 큰 숫자를 찾는 의미로 key=를 쓴다

