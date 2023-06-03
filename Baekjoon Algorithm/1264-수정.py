while True:
    s = list(str(input()))
    if s == "#":
        break
    cnt = 0
    for w in s:
        if w in 'aeiouAEIOU':
            cnt += 1
    print(cnt)