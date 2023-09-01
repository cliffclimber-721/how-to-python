li = []
num = 0

for i in range(5):
    fbi = input()
    if "FBI" in fbi:
        li.append(fbi)
if li:
    print(len(li))
else:
    print("HE GOT AWAY!")