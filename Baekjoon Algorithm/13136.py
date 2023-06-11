r, c, n = map(int, input().split())

tot_r = r // n
if r % n != 0:
    tot_r += 1

tot_c = c // n
if c % n != 0:
    tot_c += 1

print(tot_c * tot_r)