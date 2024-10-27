# 4. Determine if a number is small, medium, or large.
num = int(input("Enter a number: "))
if num > 10000:
    print("The number is large.")
elif 100 <= num <= 10000:
    print("The number is medium.")
else:
    print("The number is small.")