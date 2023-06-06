a = []

for _ in range(3):
    angle = int(input())
    a.append(angle)

if a[0] == a[1] == a[2] == 60:
    print("Equilateral")
elif (a[0] == a[1] or a[0] == a[2] or a[1] == a[2]) and sum(a) == 180:
    print("Isosceles")
elif (a[0] != a[1] != a[2]) and sum(a) == 180:
    print("Scalene")
else:
    print("Error")