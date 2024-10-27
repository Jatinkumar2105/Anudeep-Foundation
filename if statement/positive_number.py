# Input a number from the user
num = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print("num is a positive number.",num)
elif num == 0:
    print("num is neither positive nor negative.",num)
else:
    print("num is a negative number.",num)
