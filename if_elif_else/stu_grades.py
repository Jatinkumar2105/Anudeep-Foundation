# 2. Determine a student's grade based on marks.
 # Get marks from user
marks = float(input("Enter marks: ")) 
if marks >= 75:                        
    print("Grade A")
elif 65 <= marks < 75:                 
    print("Grade B")
elif 55 <= marks < 65:                
    print("Grade C")
elif 50 <= marks < 55:                 
    print("Grade D")
else:                                  
    print("Grade F")