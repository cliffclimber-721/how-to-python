caseTest = int(input())

for i in range(caseTest):
    caseScore = list(map(int, input().split()))
    dividedBy = caseScore[0]
    caseAvg = sum(caseScore[1:]) / dividedBy
    for case in caseScore:
        forPercent = len(str(case))
        forPercents = len(caseScore[1:])
        showPercent = (forPercent / forPercents) * 100

if caseAvg < case:
    print("forPercents ->", forPercents)
    print("this ->", showPercent)
caseTest -= 1