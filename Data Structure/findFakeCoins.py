def weigh(a, b, c, d): 
    if a <= fake and fake <= b:
        return -1
    elif c <= fake and fake <= d:
        return 1
    return 0

def findFakeCoins(left, right):
    if left == right:
        return left
    
    half = (right - left + 1) // 2
    g1_left = left
    g1_right = left + half - 1
    g2_left = left + half
    g2_right = g2_left + half - 1

    result = weigh(g1_left, g1_right, g2_left, g2_right)

    if result == -1:
        return findFakeCoins(g1_left, g1_right)
    elif result == 1:
        return findFakeCoins(g2_left, g2_right)
    else:
        return right

fake = int(input("Enter fake coin number: "))

n = 100
print(findFakeCoins(0, n-1))