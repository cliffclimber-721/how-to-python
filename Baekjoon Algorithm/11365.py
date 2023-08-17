while True:
    sen = input()
    if sen == "END":
        break
    else:
        print(''.join(reversed(sen)))