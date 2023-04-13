T = int(input())

for _ in range(T):
    R, S = input().split()
    for w in S:
        print(w * int(R), end='')
    print()