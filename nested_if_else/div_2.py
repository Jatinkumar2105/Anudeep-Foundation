# 7. Check if a number is divisible by 2, and if so, further check if it is divisible by 4.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is divisible by 2.")
    if number % 4 == 0:
        print("It is also divisible by 4.")
    else:
        print("It is not divisible by 4.")
else:
    print("The number is not divisible by 2.")