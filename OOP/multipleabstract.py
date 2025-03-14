# Create an abstract class Shape with two abstract methods: area() and perimeter(). 
# Implement subclasses Circle and Rectangle that provide implementations for these methods.

from abc import ABC,abstractmethod
import math

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Circle(shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        Area = math.pi * self.radius * self.radius
        print(f"The area of the circle is {Area}")
        
    
    def perimeter(self):
        per =  2 * math.pi * self.radius
        print(f"The perimeter of the rectangle is {per}")
        
        
class Rectangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        Area = self.length * self.width
        print(f"The area of the rectangle is {Area}")
    
    def perimeter(self):
        per = 2 * (self.length + self.width)
        print(f"The perimeter of the rectangle is {per}")
        
    
circle1  = Circle(7)
rectangle1 = Rectangle(4,2)

circle1.area()
circle1.perimeter()

rectangle1.area()
rectangle1.perimeter()
    