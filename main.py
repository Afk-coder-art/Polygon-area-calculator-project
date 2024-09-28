from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# 2. Rectangle class
class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# 3. Square class
class Square(Polygon):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length

# 4. Triangle class
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 2 / self.base * self.height

if __name__:
    rectangle = Rectangle(7,4)
    square = Square(4)
    triangle = Triangle(7, 3) 

    print("Rectangle area: {rectangle.calculate_area()}")
    print("Square area: {square.calculate_area()}")
    print("Triangle area: {triangle.calculate_area()}")

