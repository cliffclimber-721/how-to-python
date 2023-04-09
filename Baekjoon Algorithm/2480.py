a, b, c = map(int, input().split())

if(a == b == c):
    result1 = 10000 + a * 1000
    print(result1)
elif(a == c):
    result2 = 1000 + c * 100
    print(result2)
elif(a == b or b == c):
    result3 = 1000 + b * 100
    print(result3)
else:
    maxNum = max(a, b, c)
    result4 = maxNum * 100
    print(result4)