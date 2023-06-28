n = int(input())
a, b = map(int, (input().split()))

cola = a // 2

if cola + b > n:
    print(n)
else:
    print(cola + b)