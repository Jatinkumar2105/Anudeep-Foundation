# 6. Verify if a year is a leap year, and if so, check if it is divisible by 100 and 400.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year.")
    if year % 100 == 0 and year % 400 == 0:
        print("It is also divisible by both 100 and 400.")
else:
    print("It is not a leap year.")