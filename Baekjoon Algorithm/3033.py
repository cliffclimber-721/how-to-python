playChess = list(map(int, input().split()))
chessChar = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(chessChar[i] - playChess[i], end=" ")
        