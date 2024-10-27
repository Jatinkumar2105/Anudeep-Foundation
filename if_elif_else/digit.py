# 11. Check if a number is one-digit, two-digit, or more.
num = abs(int(input("Enter a number: ")))
if num < 10:
    print("One-digit number.")
elif 10 <= num < 100:
    print("Two-digit number.")
else:
    print("More than two digits.")