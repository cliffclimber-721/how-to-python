t = int(input())

for n in range(t):
    n, unit = map(str, input().split())
    if unit == "kg":
        print("{0:0.4f} lb".format(float(n) * 2.2046))
    elif unit == "l":
        print("{0:0.4f} g".format(float(n) * 0.2642))
    elif unit == "lb":
        print("{0:0.4f} kg".format(float(n) * 0.4536))
    elif unit == "g":
        print("{0:0.4f} l".format(float(n) * 3.7854))
