# 8. Determine if a person is employed, and if yes, check their salary range (low, medium, high).
employment_status = input("Are you employed? (yes/no): ").lower()
if employment_status == "yes":
    salary = float(input("Enter your salary: "))
    if salary < 30000:
        print("Your salary range is low.")
    elif 30000 <= salary <= 70000:
        print("Your salary range is medium.")
    else:
        print("Your salary range is high.")
else:
    print("You are not employed.")