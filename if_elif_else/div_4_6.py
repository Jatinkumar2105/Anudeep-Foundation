# 18. Check if a number is divisible by 4, 6, both, or neither.
num = int(input("Enter a number: "))
if num % 4 == 0 and num % 6 == 0:
    print("Divisible by both 4 and 6.")
elif num % 4 == 0:
    print("Divisible by 4.")
elif num % 6 == 0:
    print("Divisible by 6.")
else:
    print("Not divisible by 4 or 6.")