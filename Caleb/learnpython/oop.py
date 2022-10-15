# DRY (Don't Repeat Yourself).
# class Parrot:
#     # class attribute
#     species = "bird"

#     # instance attribute 
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color

# blu = Parrot('Blu', 10, 'Blue')
# woo = Parrot('Woo', 15, 'Red')

# print("Blu is a {}".format(blu.__class__.species))
# print("Woo is a {}".format(woo.__class__.species))

# print("{} is {} years old, and has a color of {}".format(blu.name, blu.age, blu.color))

# class Parrot:
#     # instance attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     # instance method1
#     def sing(self, song):
#         return "{} sings {} and {} years old".format(self.name, song, self.age)
#     # instance method2
#     def dance(self):
#         return "{} is now dancing".format(self.name)

# # instantiate the object
# # blu = Parrot("Blu", 10)

# # call our instance methods
# # print(blu.sing("'Happy'"))
# # print(blu.dance())


# # parent class
# class Bird:
#     def __init__(self):
#         print("Bird is ready")

#     def whoisThis(self):
#         print("Bird")

#     def swim(self):
#         print("Swim faster")

# # child class
# class Penguin(Bird):

#     def __init__(self):
#         # call super() function
#         super().__init__()
#         print("Penguin is ready")

#     def whoisThis(self):
#         print("Penguin")

#     def run(self):
#         print("Run faster")


# peggy = Penguin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()

class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

# c = Computer()
# c.sell()

# change the price 
# c.__maxprice = 1000
# c.sell()

# using the function setmaxprice
# c.setMaxPrice(1000)
# c.sell()

# c.setMaxPrice(2000)
# c.sell()

class Parrot:
    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.swim()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)