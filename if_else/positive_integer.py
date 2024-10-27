#Determine if a number is a positive integer
# Input a number from the user
num = float(input("Enter a number: "))

# Check if the number is positive and an integer
if num > 0 and num.is_integer():
    print("The number is a positive integer.")
else:
    print("The number is not a positive integer.")
