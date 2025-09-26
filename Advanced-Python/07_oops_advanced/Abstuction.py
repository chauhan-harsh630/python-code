from abc import ABC, abstractmethod

# ===============================
# Abstract Class: Shape
# ===============================
# ABC = Abstract Base Class
# An abstract class defines a blueprint for other classes.
# It can contain abstract methods that must be implemented in subclasses.
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate area of a shape.
        Must be implemented by any subclass of Shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate perimeter of a shape.
        Must be implemented by any subclass of Shape.
        """
        pass

# ===============================
# Concrete Class: Circle
# ===============================
# Implements Shape by providing specific calculations for a circle.
class Circle(Shape):
    def __init__(self, radius):
        # Radius of the circle
        self.radius = radius

    def area(self):
        # Area formula: π * r^2
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        # Perimeter (circumference) formula: 2 * π * r
        return 2 * 3.14 * self.radius

# ===============================
# Concrete Class: Square
# ===============================
# Implements Shape by providing specific calculations for a square.
class Square(Shape):
    def __init__(self, side):
        # Length of a side of the square
        self.side = side

    def area(self):
        # Area formula: side^2
        return self.side * self.side

    def perimeter(self):
        # Perimeter formula: 4 * side
        return 4 * self.side

# ===============================
# Usage / Testing
# ===============================
# We can store different shapes in a single list and call their methods
# Polymorphism: area() and perimeter() behave differently depending on the object type
shapes = [Circle(5), Square(4)]

for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")
