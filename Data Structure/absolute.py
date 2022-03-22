import math

# 1. If "a" is a positive, prints "a", if it is a negative, prints "-a"
def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a

# 2. This is a usage of square root, so the results are printed by decimal points.
def abs_sqr(a):
    b = a * a
    return math.sqrt(b)

print(abs_sign(-1))
print(abs_sign(10))
print(abs_sqr(4))
print(abs_sqr(-5))