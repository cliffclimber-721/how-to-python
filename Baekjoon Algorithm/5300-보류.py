n = int(input())
st = 0
li = []

while st < n:
    st += 1
    li.append(st)
    if st % 6  == 0:
        li.append("Go!")

print(li)