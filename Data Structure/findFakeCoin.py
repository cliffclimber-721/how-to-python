# 입력은 전체 동전 위치의 시작과 끝(0, n-1)
# 출력은 가짜 동전의 위치 번호

# a~b까지 놓은 동전과 c~d까지 놓은 동전 무게를 비교하는데
# a~b사이에 가짜 동전이 있으면, 즉 가벼우면 -1
# c~d사이에 가짜 동전이 있으면, 즉 가벼우면 1
# 가짜 동전이 없으면 0

fake = int(input("Enter fake coin to find: "))

def weigh(a, b, c, d): 
    if a <= fake and fake <= b:
        return -1
    elif c <= fake and fake <= d:
        return 1
    return 0

# left에서 right까지 놓인 가짜 동전의 위치를 찾아낸다
def findFakeCoin(left, right):
    for i in range(left+1, right+1): # left+1부터 right까지 다 비교한다
        result = weigh(left, left, i, i) # 가장 왼쪽 동전과 나머지 동전을 비교하는 weigh
        if result == -1: # 가벼우면
            return left
        elif result == 1: # i가 가벼우면
            return i
        
    return -1


n = 100
print(findFakeCoin(0, n-1))