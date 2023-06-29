tots = 0

while True:
    try:
        way, stair = input().split()
        if way == "Es":
            tots += int(stair) * 21
        elif way == "Stair":
            tots += int(stair) * 17
    except:
        break

print(tots)