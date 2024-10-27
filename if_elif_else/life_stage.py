# 8. Determine a person’s life stage based on age.
age = int(input("Enter age: "))
if age <= 12:
    print("Life stage: Child")
elif 13 <= age <= 19:
    print("Life stage: Teen")
elif 20 <= age <= 64:
    print("Life stage: Adult")
else:
    print("Life stage: Senior")