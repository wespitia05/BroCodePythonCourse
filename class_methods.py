# class methods: allows operations related to the class itself
#           take (cls) as the first parameter, which represents the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        # whenever we construct a student object, increase count by 1
        Student.count += 1
        Student.total_gpa += gpa
    
    # instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls): # instead of self, we use cls
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"
    
student1 = Student("Spongebob", 3.2)
student1 = Student("Patrick", 2.0)
student1 = Student("Sandy", 4.0)
    
print(Student.get_count())
print(Student.get_average_gpa())