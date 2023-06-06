S_total = list(map(int, input().split()))
T_total = list(map(int, input().split()))

if sum(S_total) > sum(T_total) or sum(S_total) == sum(T_total):
    print(sum(S_total))
elif sum(S_total) < sum(T_total):
    print(sum(T_total))