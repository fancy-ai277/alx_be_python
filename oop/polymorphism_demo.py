import math

class Shape:
    """Base class representing a geometric shape."""

    def area(self):
        """Method to be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement the area method.")


class Rectangle(Shape):
    """A class representing a rectangle."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    """A class representing a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of a circle."""
        return math.pi * (self.radius ** 2)
