#xndir 1
import math

class Shape:
    def init(self, name):
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass

class TwoDShape(Shape):
    def init(self, name):
        super().init(name)

class ThreeDShape(Shape):
    def init(self, name):
        super().init(name)

class Circle(TwoDShape):
    def init(self, name, radius):
        super().init(name)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(TwoDShape):
    def init(self, name, width, height):
        super().init(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Sphere(ThreeDShape):
    def init(self, name, radius):
        super().init(name)
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

class Cuboid(ThreeDShape):
    def init(self, name, length, width, height):
        super().init(name)
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self):
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

    def volume(self):
        return self.length * self.width * self.height

# Example usage:
circle = Circle("Circle", 5)
rectangle = Rectangle("Rectangle", 4, 6)
sphere = Sphere("Sphere", 3)
cuboid = Cuboid("Cuboid", 2, 3, 4)

print(f"{circle.name} - Area: {circle.area()}, Perimeter: {circle.perimeter()}")
print(f"{rectangle.name} - Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")
print(f"{sphere.name} - Surface Area: {sphere.surface_area()}, Volume: {sphere.volume()}")
print(f"{cuboid.name} - Surface Area: {cuboid.surface_area()}, Volume: {cuboid.volume()}")