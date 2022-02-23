square = int(input("Enter the number to square : ")) # show ranges for square

num = 1 # default number for square

while square >= num: # if "square" range is smaller than "num"
    print(num, num * num)
    num = num + 1 # increase the default number because it has to be work until "square" range