from datetime import date

class Student:
    # Class Variables: defined outside the constructor but within the class
    school_name: str = "AltSchool Africa"

    # Constructor to Initialize the Object
    def __init__(self, name: str, course: str, age: int):
        self.name = name
        self.course = course
        self.age = age
    
    # Instance Method: uses parameters from the constructor
    def show(self):
        return f"Student Name: {self.name}; Course: {self.course}; Age: {self.age}"
    
    # Static Method: does not interact with the class. Uses the decorator @staticmethod
    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

    # Class Method: to use a class variable, wrap the function in @classmethod, with cls as the parameter
    @classmethod
    def get_school_name(cls):
        return cls.school_name
    
    @classmethod
    def get_age_from_birth_year(cls, name: str, course: str, birth_year: int):
        return f'Name: {name}, Course: {course}, Age: {date.today().year - birth_year}'

# Testing the Class
student = Student('Austin', 'Python', 27)
print(student.name)
print(student.course)
print(student.age)
print(student.show())

if Student.is_adult(20):
    print('This student is an adult')
else:
    print('This student is not an adult')

print(Student.get_school_name())

print(Student.get_age_from_birth_year('Austin', 'Python', 1995))