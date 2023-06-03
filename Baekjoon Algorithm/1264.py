while True:
    s = list(str(input()))
    cnt = 0
    if "#" in s:
        break
    for w in s:
        if w in "aeiouAEIOU":
            cnt += 1
    print(cnt)