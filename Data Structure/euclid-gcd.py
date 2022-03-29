def euclid_gcd(num1, num2):
    print("euclid gcd: ", num1, num2)
    if num2 == 0:
        return num1
    return euclid_gcd(num2, num1 % num2)

print(euclid_gcd(17, 34))
print(euclid_gcd(20, 45))