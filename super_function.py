# super() is a function used in a child class to call methods from a parent class (superclass)
#   allows you to extend the functionality of the inherited methods

# since filled and color are used in all three classes, we will put them into a parent class
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    # extend functionality
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

# for each class we need to instantiate an object
class Circle(Shape):
    def __init__(self, color, filled, radius):
        # inside constructor of children classes, we call constructor of super class
        super().__init__(color, filled)
        self.radius = radius
    
    # method overwriting
    def describe(self):
        print(f"it is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, color, filled, width):
        # inside constructor of children classes, we call constructor of super class
        super().__init__(color, filled)
        self.width = width
    
    def describe(self):
        print(f"it is a square with an area of {self.width * self.width}cm^2")

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        # inside constructor of children classes, we call constructor of super class
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"it is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()

circle = Circle(color = "Red", filled = True, radius = 5)
print(circle.color, circle.filled, f"{circle.radius}cm")

square = Square(color = "Blue", filled = False, width = 6)
print(square.color, square.filled, f"{square.width}cm")

triangle = Triangle(color = "Yellow", filled = True, width = 7, height = 8)
print(triangle.color, triangle.filled, f"{triangle.width}cm", f"{triangle.height}cm")

circle.describe()
square.describe()
triangle.describe()