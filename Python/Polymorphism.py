class Shape:
    def area(self):
        print("Diffrent Shapes have different Areas")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14*(self.radius)**2

class Rectangle(Shape):
    def __init__(self, len, wid):
        self.len = len
        self.wid = wid
    
    def area(self):
        return self.len*self.wid

s = Shape()
s.area()
c = Circle(10)
print(c.area())
r = Rectangle(10, 12)
print(r.area())