import math
a = int(input("Enter a:"))
b = int(input("Enter b:"))
if a<=1000 and b<=1000:
    print("Hypotenuse:", math.sqrt(a**2+b**2))
else:
    print("More than 1000 entered data")

