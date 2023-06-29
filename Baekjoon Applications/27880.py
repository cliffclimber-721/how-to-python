tots = 0

for _ in range(4):
    way, stair = input().split()
    # 이게 뭔 코드지...
    tots += int(stair) * [21, 17][way == "Stair"]

print(tots)