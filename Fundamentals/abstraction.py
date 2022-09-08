from abc import ABC, abstractmethod
from math import pi
from xml.etree.ElementTree import PI

class Shape(ABC): # Abstract class inherits from ABC, the base class for abstraction
    @abstractmethod # This is the decorator used for abstract methods
    def area(self): # Abstract Method
        pass

    @abstractmethod
    def volume(self):
        pass

class Square(Shape): # When inheriting from an abstract class, you have to implement all of its methods
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def volume(self):
        return self.side ** 3

class Circle(Shape):
    PI = 3.14 # Class Constant

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.PI * (self.radius ** 2)
    
    def volume(self):
        return self.PI * (self.radius ** 3)

if __name__ == "__main__":
    square = Square(6)
    # print('Area of this square is {}, and its volum is {}'.format(square.area(), square.volume()))
    circle = Circle(2)
    # print(f"Area of this circle is {circle.area()} and its volume is {circle.volume()}")