import math
a = 5
b = 5
c = 6
perimeter = a + b + c
s = perimeter / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Perimeter of a triangle: ", round(perimeter, 2))
print("Area of the triangle: ", round(area, 2))