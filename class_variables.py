# class varaibles = shared among all instances of a class
# defined outside the constructor
# allows you to share data among all objects created from that class

class Student:
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(student1.name)
print(student1.age)
# access class variable through class instance
print(Student.class_year)

print(student2.name)
print(student2.age)
# access class variable through class instance
print(Student.class_year)

print(student3.name)
print(student3.age)
# access class variable through class instance
print(Student.class_year)

print(student4.name)
print(student4.age)
# access class variable through class instance
print(Student.class_year)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")