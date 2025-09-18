# abstract class: a class that cannot be instantiated on its own; meant to be subclassed
#   they can contain abstract methods, which are declared but have no implementation
#   benefits: prevents instantiation of the class itself & requires children to use inherited abstract methods

# abc - abstract base classes
# ABC - abstract base class
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")
    
    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You drive the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

# boat class cannot function bc it needs both go and stop methods
class Boat(Vehicle):
    def go(self):
        print("You sail the boat")
    
    # def stop(self):
        # print("You anchor the boat")

car = Car()

car.go()
car.stop()

motorcycle = Motorcycle()

motorcycle.go()
motorcycle.stop()

boat = Boat()