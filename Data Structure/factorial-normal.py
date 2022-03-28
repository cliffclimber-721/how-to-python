def factorial(num):
    fac = 1 # initialising number
    for i in range(1, num + 1):
    # starting from 1 to " num + 1 "; why range is " num + 1 " => if it is just " num ",
    # range cannot reach it.
        fac = fac * i # multiple it
    return fac

print(factorial(1))
print(factorial(3))
print(factorial(5))