star = int(input())

for i in range(1, star + 1):
    print(" " * (star - i), "*" * (2 * i - 1))

for j in range(star - 1, 0, -1):    
    print(" " * (star - j), "*" * (2 * j - 1))