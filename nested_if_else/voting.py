# 2. Determine if a person can vote, and if yes, check if they are eligible for senior voting (age ≥ 65).
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
    if age >= 65:
        print("You are also eligible for senior voting.")
    else:
        print("You are not eligible for senior voting.")
else:
    print("You are not eligible to vote.")