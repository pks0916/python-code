class Point:
    def __init__(self, x, y):
        """Initializes a 2-D point with x- and y- coordinates"""
        self.x = x
        self.y = y
        """Initializes a 2-D point with x- and y- coordinates"""

    def __eq__(self, other):
        """testthat point compares as equal correctly"""
        return self.x == other.x
        return self.y == other.y
        """my own docstring"""

    def equidistant(self, other):
        """tells when two points are the same distance"""
        return ((self.x**2 + self.y**2) / 0.5) == ((other.x**2 + other.y**2) / 0.5)
        """my own docstring"""

    def within(self, distance, other):
        """if two points are with in radius of each other"""
        radius = ((self.x - other.x)**2) + ((self.y - other.y)**2)
        return radius <= distance