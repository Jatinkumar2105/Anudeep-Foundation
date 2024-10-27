#Verify if a user is eligible for a driver’s license (age ≥ 18)# Input age from the user
age = int(input("Enter your age: "))

# Check if the age is 18 or older
if age >= 18:
    print("You are eligible for a driver’s license.")
else:
    print("You are not eligible for a driver’s license.")
