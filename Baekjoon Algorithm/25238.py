a, b = map(int, input().split())

tot = a - (a * b / 100)

if tot >= 100:
    print("0")
else:
    print("1")