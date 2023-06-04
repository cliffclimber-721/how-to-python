tot, sub = map(int, input().split())

if tot < sub:
    print("-1")

else:
    s1 = (tot + sub) // 2
    s2 = tot - s1
    print(s1, s2)