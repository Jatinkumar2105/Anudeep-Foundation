# 15. Check if a person is a child, adolescent, or adult based on age.
age = int(input("Enter age: "))
if age <= 12:
    print("Child")
elif 13 <= age <= 17:
    print("Adolescent")
else:
    print("Adult")