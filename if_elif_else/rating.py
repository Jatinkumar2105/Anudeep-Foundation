# 17. Assign a performance rating based on a percentage.
percentage = float(input("Enter the percentage: "))
if percentage >= 90:
    print("Performance: Excellent")
elif 75 <= percentage < 90:
    print("Performance: Good")
elif 50 <= percentage < 75:
    print("Performance: Average")
else:
    print("Performance: Poor")