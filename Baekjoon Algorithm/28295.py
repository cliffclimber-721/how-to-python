dirs = ["N", "E", "S", "W"]
res = "N"

for _ in range(10):
    com = int(input())
    if com == 1:
        res = dirs[(dirs.index(res) + 1) % 4]
    elif com == 2:
        res = dirs[(dirs.index(res) + 2) % 4]
    elif com == 3:
        res = dirs[(dirs.index(res) + 3) % 4]

print(res)