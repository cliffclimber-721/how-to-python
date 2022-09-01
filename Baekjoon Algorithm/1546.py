num = int(input())
score = list(map(int, input().split()))
maxScore = max(score)

# 새로운 계산법은 전체 점수를 다 더하고 최고점을 나눈 후 100을 곱하고 그 전체 계산을 과목 개수로 나눈다.
newAvg = (sum(score) / maxScore * 100)/num
print(newAvg)