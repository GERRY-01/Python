# Create an abstract class Employee with a constructor that takes name and salary as parameters.
# Add an abstract method calculate_bonus(). Implement a subclass Manager that calculates a 20% bonus.

from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    @abstractmethod
    def calculate_bonus(self):
        pass
    
class Manager(Employee):
    def calculate_bonus(self):
        final_salary = self.salary + (self.salary * 0.2)
        print(f"{self.name}'s salary after the bonus is {final_salary}")
        
manager1 = Manager("Gerry",80000)
manager1.calculate_bonus()