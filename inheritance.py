# inheritance = allows class to inherit attributes and methods from another class
# helps with code reusability and extensibility
# class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is asleep")
    
class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEAK!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()

# print(cat.name)
# print(cat.is_alive)
# cat.eat()
# cat.sleep()

# print(mouse.name)
# print(mouse.is_alive)
# mouse.eat()
# mouse.sleep()

dog.speak()
cat.speak()
mouse.speak()