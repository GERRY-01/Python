from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
        
    def stop(self):
        print("The car is stopping")
        
        
class car(vehicle):
    def start(self):
        print("The car started")

class bike(vehicle):
    def start(self):
        print("The bike started")

car1 = car()
bike1 = bike()

car1.start()
bike1.start()
