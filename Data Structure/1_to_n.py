number = int(input("give your number: "))

def sumIt(n):
    sum = 0 # you need to give 0 to initialize
    for i in range(1, n+1): # range is given with variable "i" because the values has to be stored in other place.
        sum += i # Initialized number is here, and "i" is used because of "for-in-range". "n" is just an input for the range.
    return sum

print(sumIt(number))