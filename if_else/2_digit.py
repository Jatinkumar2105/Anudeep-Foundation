#Check if a number is a two-digit number
# Input a number from the user
num = int(input("Enter a number: "))

# Check if the absolute value of the number is between 10 and 99
if 10 <= abs(num) < 100:
    print("The number is a two-digit number.")
else:
    print("The number is not a two-digit number.")
