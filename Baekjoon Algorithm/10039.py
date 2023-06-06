score = 0

for _ in range(5):
    s = int(input())
    if s < 40:
        s = 40
    
    score += s

print(score // 5)