n = int(input())
fin = n % 8

if fin == 1:
    print(1)
elif fin == 2 or fin == 0:
    print(2)
elif fin == 3 or fin == 7:
    print(3)
elif fin == 4 or fin == 6:
    print(4)
else:
    print(5)