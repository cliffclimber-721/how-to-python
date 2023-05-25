number = map(int, input().split())
total = 0

for i in number:
    sq = i * i
    total += sq

rem = total % 10 
print(rem)