#Check if a password matches a stored password
# Define a stored password
stored_password = "jatin123"  # Replace with the actual stored password

# Input password from the user
password = input("Enter your password: ")

# Check if the entered password matches the stored password
if password == stored_password:
    print("Password matches.")
else:
    print("Password does not match.")
