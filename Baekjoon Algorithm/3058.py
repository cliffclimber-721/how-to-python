n = int(input())

for _ in range(n):
    tot_li = []
    li = list(map(int, input().split()))
    for i in range(len(li)):
        if int(li[i]) % 2 == 0:
            tot_li.append(li[i])
    print(sum(tot_li), min(tot_li))