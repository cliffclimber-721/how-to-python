c = int(input())

for _ in range(c):
    s = list(map(int, input().split()))
    sc = 0
    for score in s[1:]:
        avg = sum(s[1:]) / s[0]
        if score > avg:
            sc += 1
    per = sc / len(s[1:]) * 100

    print("{0:0.3f}%".format(per))