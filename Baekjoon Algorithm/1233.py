s1, s2, s3 = map(int, input().split())
tot = []

for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            res = i + j + k
            tot.append(res)

print(max(set(tot), key=tot.count))
