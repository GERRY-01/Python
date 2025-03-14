#Create an abstract class Flyable with an abstract method fly(). 
# Create another abstract class Swimmable with an abstract method swim().
# Implement a subclass Duck that inherits from both Flyable and Swimmable.

from abc import ABC,abstractmethod
 
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass
    
class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass
    
class Duck(Flyable,Swimmable):
    def fly(self):
        print("The duck can fly")
        
    def swim(self):
        print("The duck can swim")
        
duck1  = Duck()
duck1.fly()
duck1.swim()

