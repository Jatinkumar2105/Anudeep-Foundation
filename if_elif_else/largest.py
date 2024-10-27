# 14. Determine the largest of three given numbers.
a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
c = int(input("enter number 3:"))
if a >= b and a >= c:
    print("The largest number is ",a)
elif b >= a and b >= c:
    print("The largest number is ",b)
else:
    print("The largest number is ",c)