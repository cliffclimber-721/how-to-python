for_check = [i for i in range(1, 31)]

for c in range(28):
    check = int(input())
    for_check.remove(check)

print(min(for_check))
print(max(for_check))