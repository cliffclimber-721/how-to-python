N = input()
ppl = list(map(int, input().split()))
sets = set(ppl)

print(len(ppl) - len(sets))