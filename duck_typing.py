# duck typing: another way to achieve polymorphism besides inheritance
# object must have the minimum necessary attributes/methods
# if it looks like a duck and quacks like a duck, it must be a duck

class Animal:
    # if youre an animal, you are alive
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = False
    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)