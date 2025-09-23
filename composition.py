# aggregation: a relationship where one object contains references to other independent objects
# "has-a" relationship

# composition: the composed object directly owns its components, which cannot exist independently
# "owns-a" relationship

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

# composed class
class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        # for single wheel
        self.wheel = Wheel(wheel_size)
        # for multiple wheels
        # creates 4 wheel objects
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"

car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)

print(car1.display_car())
print(car2.display_car())