import math

class Circle:
    def __init__(self, x, y, r):
        "function to set the radius to ensure positivity is checked"
        self.x = x
        self.y = y
        self.set_r(r)
    
    def length(self):
        "returns the length of a circle"
        return 2 * math.pi * self.r
    
    def square(self):
        "returns the area of ​​a circle"
        return math.pi * self.r**2
    
    def set_r(self, r):
        "sets the radius of the circle"
        assert r > 0, "The radius must be a positive number!"
        self.r = r

c = Circle(3, 4, 1)
print(c.length(), c.square())  

c.set_r(-1) #checks that the given radius r is a positive number and sets its value

