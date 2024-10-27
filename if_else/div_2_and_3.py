#Check if a number is divisible by both 2 and 3
# Input a number from the user
num = int(input("Enter a number: "))

# Check if the number is divisible by both 2 and 3
if num % 2 == 0 and num % 3 == 0:
    print("The number is divisible by both 2 and 3.")
else:
    print("The number is not divisible by both 2 and 3.")
