t = int(input())

for c in range(t):
    c = int(input())
    q = c // 25
    qr = c % 25
    d = qr // 10
    dr = qr % 10
    if dr < 5:
        n = 0
        p = dr
    else:
        n = dr // 5
        nr = dr % 5
        p = nr

    print(q, d, n, p)