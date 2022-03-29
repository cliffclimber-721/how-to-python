def gcd(num1, num2):
    value = min(num1, num2) # find the minimum value
    while True:
        if num1 % value == 0 and num2 % value == 0:
            return value
        value = value - 1

print(gcd(15, 5))
print(gcd(47, 23))