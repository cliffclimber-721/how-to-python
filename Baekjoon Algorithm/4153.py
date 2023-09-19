while True:
    n = list(map(int, input().split()))
    if sum(n) == 0:
        break
    mx = max(n)
    n.remove(mx)
    if n[0] ** 2 + n[1] ** 2 == mx ** 2:
        print("right")
    else:
        print("wrong")