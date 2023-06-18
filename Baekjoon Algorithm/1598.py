a, b = map(int, input().split())

# -1 빼주는 이유는 좌표 개념으로 접근하기 위함
a -= 1
b -= 1

w = abs(a//4 - b//4)
h = abs(a%4 - b%4)
print(w + h)