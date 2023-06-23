n, k = map(int, input().split())
num_list = []

for i in range(n):
    r = n % (i+1) # 나머지 출력
    if r == 0:
        num_list.append(i+1)

if len(num_list) < k:
    print("0")
else:
    print(num_list[k-1])