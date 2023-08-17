limit = int(input())
record = int(input())
fine = int(record - limit)

if 1 <= fine <= 20:
    print("You are speeding and your fine is $100.")
elif 21 <= fine <= 30:
    print("You are speeding and your fine is $270.")
elif fine >= 31:
    print("You are speeding and your fine is $500.")
else:
    print("Congratulations, you are within the speed limit!")