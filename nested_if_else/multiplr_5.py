# 5. Check if a number is positive, and if yes, further check if it is a multiple of 5.
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
    if num % 5 == 0:
        print("It is also a multiple of 5.")
    else:
        print("It is not a multiple of 5.")
else:
    print("The number is not positive.")