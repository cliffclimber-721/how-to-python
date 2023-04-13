n1, n2 = input().split()
nr1 = n1[::-1]
nr2 = n2[::-1]

if(nr1 > nr2):
    print(nr1)
else:
    print(nr2)