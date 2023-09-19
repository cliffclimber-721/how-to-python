t = int(input())

for _ in range(t):
    jb = int(input())
    for i in range(jb):
        if i == 0:
            print("#" * jb)
        elif i != 0 and i != (jb-1):
            print("#" + "J" * (jb-2) + "#")
        else:
            print("#" * jb)
    print()