sci = []
his = []

for s in range(4):
    s = int(input())
    sci.append(s)

for h in range(2):
    h = int(input())
    his.append(h)

print((sum(sci) - min(sci)) + (sum(his) - min(his)))