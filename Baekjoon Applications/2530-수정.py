A, B, C = map(int, input().split())
D = int(input())

sec = D % 60
min = D // 60

final_sec = C + sec
final_min = B + min

if final_sec == 60:
    print("0")
print(A, final_min, final_sec)