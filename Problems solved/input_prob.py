input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

def added(num1, num2):
    return num1+num2

print("두 수의 합은 %s 입니다" % added(input1, input2))