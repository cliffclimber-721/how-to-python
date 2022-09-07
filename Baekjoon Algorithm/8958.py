num = int(input())

for _ in range(num):
    oxQuiz = list(input())
    oxScore = 0
    finalScore = 0
    for i in oxQuiz:
        if i == "O":
            oxScore += 1
            finalScore += oxScore
        else:
            oxScore = 0
    print(finalScore)