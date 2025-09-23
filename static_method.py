# static methods: a method that belongs to a class rather than any object from that class (instance)
# usually used for general utility functions

# instance methods: best for operations on instances of the class (objects)
# static methods: best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Frycook", "Janitor"]
        # check if position we receive is in the positions list
        return position in valid_positions
    
employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Frycook")
    
# for static method, you only need to access that class
print(Employee.is_valid_position("Frycook")) # True
print(Employee.is_valid_position("Rocket Scientist")) # False

# for instance method, you access an object then call the instance method
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())