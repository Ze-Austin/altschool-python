class Student:
    def __init__(self, name = str, score = int, matric_no = str):
        self.name = name # Public variable: accessed within and outside the class
        self._score = score # Protected variable: accessed only within the class and its subclasses
        self.__matric_no = matric_no # Private variable: accessed only within the class
    
    # This is a getter: it reads the value already assigned to the attribute
    @property
    def score(self):
        return self._score
    
    # Protected method can only be called by other methods in the same class and its subclasses
    # This is a setter: it puts a new value for the attribute
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise TypeError("Score must be an integer")
        self._score = value
    
    # Private method can only be called by other methods in same class; can't be accessed by its subclasses
    def __display(self):
        print('Name: {}, Score: {}, Matric No.: {}'.format(self.name, self._score, self.__matric_no))
    
    # Here's a public instance method calling the private method
    def display(self):
        self.__display()


if __name__ == '__main__':
    s = Student('John', 87, '070922001')
    s.display()
    # print(s.score)
    s.score = 77
    print('\nScore has been changed to {}\n'.format(s.score))
    s.display()
    # print(s.__matric_no) doesn't work because __matric.no is a private variable
    # print(s.__display()) doesn't work because __display() is a private method