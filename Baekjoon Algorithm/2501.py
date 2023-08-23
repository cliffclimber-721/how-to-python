n, k = map(int, input().split())
li = []

for i in range(n):
    r = n % (i+1) # 나머지 출력
    if r == 0:
        li.append(i+1)

if len(li) < k:
    print("0")
else:
    print(li[k-1])