# 4. Verify if a student has passed a subject, and if passed, check if they scored distinction (≥ 75).
marks = float(input("Enter marks: "))
if marks >= 50:
    print("The student has passed.")
    if marks >= 75:
        print("They scored a distinction.")
    else:
        print("They did not score a distinction.")
else:
    print("The student has failed.")