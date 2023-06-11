# 도대체 뭐가 틀린거지...

r, c, n = map(int, input().split())

tot_r = r // n
tot_c = c // n

if tot_r != 0:
    print((tot_r + 1) * tot_c)
elif tot_c != 0:
    print((tot_c + 1) * tot_r)
else:
    print(tot_c * tot_r)