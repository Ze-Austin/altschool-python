class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def get_person_info(self):
        print(f"{self.name} is {self.age} years old")
    
    def random_method(self):
        return f"This is a random method from Person"

class School:
    def __init__(self, school_name: str, school_location: str):
        self.school_name = school_name
        self.school_location = school_location
    
    def get_school_info(self):
        print(f"{self.school_name} is in {self.school_location}")
    
    def random_method(self):
        return f"This is a random method from School"

class Student(Person, School):
    def __init__(self, name: str, age: int, school_name: str, school_location: int):
        Person.__init__(self, name, age)
        School.__init__(self, school_name, school_location)
    
    def get_student_info(self):
        print(f"{self.name} attends {self.school_name}")

if __name__ == "__main__":
    student = Student("Austin", 27, "AltSchool Africa", "California")
    student.get_person_info()
    student.get_school_info()
    student.get_student_info()
    print(student.random_method())

''' 
When the same method inherited by a child class appears in multiple parent classes, Python will read from left to right and prioritise the leftmost parent called when defining the subclass. Here, it's Person before School in class Student(Person, School)
'''