for _ in range(3):
    yut = list(map(int, input().split()))
    
    if yut.count(0) == 1:
        print("A")
    elif yut.count(0) == 2:
        print("B")
    elif yut.count(0) == 3:
        print("C")
    elif yut.count(0) == 4:
        print("D")
    elif yut.count(1) == 4:
        print("E")