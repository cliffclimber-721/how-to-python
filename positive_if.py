default = 0

while True:
    addNum = int(input("Add the number : "))
    if addNum < 0:
        break
    else:
        default += addNum

print(default)