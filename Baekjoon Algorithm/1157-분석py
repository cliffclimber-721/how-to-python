w = input().lower()
wl = list(set(w))
cnt = []

for i in wl:
    count = w.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(wl[(cnt.index(max(cnt)))].upper())