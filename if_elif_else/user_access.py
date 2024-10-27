# 7. Verify a user’s access level.
role = input("Enter your role (admin, user, guest): ").lower()
if role == 'admin':
    print("Access level: Admin")
elif role == 'user':
    print("Access level: User")
else:
    print("Access level: Guest")