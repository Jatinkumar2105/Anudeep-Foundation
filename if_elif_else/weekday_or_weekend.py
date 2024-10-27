# 5. Check if a day is a weekday or weekend.
day = input("Enter the day of the week: ").lower()
if day in ['saturday', 'sunday']:
    print("It's the weekend.")
else:
    print("It's a weekday.")