n = int(input())

for _ in range(n):
    x = int(input())
    if x % 2 == 0:
        print("{0} is even".format(x))
    else:
        print("{0} is odd".format(x))