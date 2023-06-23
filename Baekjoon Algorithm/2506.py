n = int(input())
s = list(map(int, input().split())) # for 문 안에 넣어주면,,, n만큼 뽑아내야한다,,
tot = 0
cnt = 0

for i in range(n):
    if s[i] == 1:
        cnt += 1
    else:
        cnt = 0
    tot += cnt

print(tot)