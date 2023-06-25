# 딕셔너리를 사용하지 않아도,, 가능하다

color = ["black" , "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

o1 = color.index(input())
o2 = color.index(input())
o3 = color.index(input())

print(int(str(o1) + str(o2)) * (10 ** o3))