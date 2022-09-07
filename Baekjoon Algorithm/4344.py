caseTest = int(input())

for i in range(caseTest):
    caseScore=list(map(int,input().split()))
    caseTest = 0
    for j in caseScore[1:]:
        caseAvg = sum(caseScore[1:])/caseScore[0]
        if j > caseAvg:
            caseTest += 1
    forPercent = caseTest / caseScore[0]*100
    print('{0:0.3f}%'.format(forPercent))