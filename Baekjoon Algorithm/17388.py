s, k, h = map(int, input().split())
tot = []

if s + k + h >= 100:
    print("OK")
elif s + k + h < 100:
    tot.append(s);tot.append(k);tot.append(h)  
    if min(tot) == s:
        print("Soongsil")
    elif min(tot) == k:
        print("Korea")
    else:
        print("Hanyang")