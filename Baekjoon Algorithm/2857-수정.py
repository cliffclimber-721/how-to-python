li = []

for i in range(5):
    find = input()
    if "FBI" in find:
        li.append(i)

if len(li) == 0:
    print("HE GOT AWAY!")
else:
    print(*li)