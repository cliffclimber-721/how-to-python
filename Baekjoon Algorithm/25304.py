x = int(input())
n = int(input())

all_price = 0
for i in range(n):
    x1, x2 = map(int, input().split())
    price = x1 * x2
    all_price = all_price + price

if(all_price == x):
    print("Yes")
else:
    print("No")