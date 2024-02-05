c, d = map(int, input().split())
pars = []

parstel = 30 * c + 40 * d
parscell = 35 * c + 30 * d
parsphone = 40 * c + 20 * d

while c > 0 and d > 0:
    pars.append(parstel)
    pars.append(parscell)
    pars.append(parsphone)
    if c == 0 and d == 0:
        break

print(max(pars))