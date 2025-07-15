class Shape:
    def area(self):
        return "yuzani kiritish formulasi"
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        yuza = 3.14 * self.radius**2
        return f"aylananing yuzasi  = {yuza:.2f}"

class Rectangle(Shape):
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
    def area(self):
        yuza = self.a1 *self.a2
        return f"Tortburchakning yuzi = {yuza:.2f}"
    
class Triangle(Shape):
    def __init__(self,a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
    def area(self):
        s = (self.a1 +self.a2 + self.a3) / 2
        yuza = (s*((s-self.a1)* (s - self.a2) * (s - self.a3)))**0.5
        return f"uchburchakning yuzi = {yuza:2f}"

        
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)

print(circle.area())
print(rectangle.area())
print(triangle.area())  