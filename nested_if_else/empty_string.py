# 3. Check if a string is non-empty, and if so, verify if it contains more than 10 characters.
text = input("Enter a string: ")
if text:
    print("The string is not empty.")
    if len(text) > 10:
        print("It contains more than 10 characters.")
    else:
        print("It contains 10 or fewer characters.")
else:
    print("The string is empty.")