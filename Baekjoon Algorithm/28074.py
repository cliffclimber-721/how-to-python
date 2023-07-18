word = input()

for l in "MOBIS" :
    if l not in word :
        print("NO")
        break
else: 
    print("YES")