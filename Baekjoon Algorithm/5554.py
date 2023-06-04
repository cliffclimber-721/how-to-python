to_school = int(input())
to_pc = int(input())
to_ac = int(input())
to_home = int(input())

tot = to_school + to_pc + to_ac + to_home
tot_min = tot // 60
tot_sec = tot % 60

print(tot_min)
print(tot_sec)