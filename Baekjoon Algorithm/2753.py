# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
lunar=int(input())

if lunar%4==0 and lunar%100 != 0 or lunar%400 == 0:
    print("1")
else:
    print("0")