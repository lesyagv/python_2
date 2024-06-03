import math
a = float(input("Enter the length of the first side of the triangle: "))
b = float(input("Enter the length of the other side of the triangle: "))
c = float(input("Enter the length of the third side of the triangle: "))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Area of a triangle: ", round(area, 2))