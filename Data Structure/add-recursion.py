def add_recursion(num):
    if num <= 1:
        return 1
    return num + add_recursion(num - 1)

print(add_recursion(10))