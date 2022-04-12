pwd = "skywalker"
pwd_correct = 0

while pwd_correct < 3:
    pwd_input = input("Enter password : ")
    if pwd == pwd_input:
        print("Login Success!")
        break

    elif pwd != pwd_input and pwd_correct < 2:
        print("Wrong password.")
    pwd_correct += 1

else:
    print("Login Fail!")