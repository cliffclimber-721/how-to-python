while True:
    num = input()
    tot = 1
    
    if num == '0':
        break
    for i in num:
        if i == '0':
            tot += 4
        elif i == '1':
            tot += 2
        else:
            tot += 3
        tot += 1
    print(tot)