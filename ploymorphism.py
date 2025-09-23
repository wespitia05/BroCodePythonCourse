# polymorphism is the greek word for "have many forms or faces"
# poly = many   |    morph = form

# two ways to achieve polymorphism:
#   1. inheritance: an object could be treated of the same type as a parent class
#   2. duck typing: object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height * 0.5

# its a circle and a shape, but not a square or triangle
# circle = Circle()
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        # use superclass to get radius from circle method
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("Pepperoni", 15)]

# loop through each shape in shapes
for shape in shapes:
    print(f"{shape.area()} cm^2")