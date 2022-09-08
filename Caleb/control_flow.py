# Control Flow
# if condition:
#     Statement_1
#     Statement_2
#     Statement_3
# Statement
# IF Statement
# num = int(input('Enter any number: '))
# if (num%5==0):
#     print(f'Given number {num} is divisible by 5')
#     print('This statement belong to the if statement')

# print('This statement does not belong to if statement')

# a = 30
# b = 20

# if b > a:
#     print('b is greater than a')
# print('this is false')

# IF-ELSE Statement
# a = 20
# b = 30

# if b > a:
#     print('b is greater than a')
# else:
#     print('this is false')

# Check if a number is Even number or not
# num = int(input('Enter any number: '))
# if num % 2 ==0:
#     print(f'The number {num} is an Even number')
# else:
#     print(f'The number {num} is an Odd number')

#ELIF Statement
# if condition_1:
#     Statement_1
#     Statement_2
# elif condition_2:
#     Statement_3
#     Statement_4
# else:
#     Statement_5
#     Statement_6

# a = int(input('Enter any First number: '))
# b = int(input('Enter any Second number: '))

# if b > a:
#     print(f'{b} is greater than {a}')
# elif b < a:
#     print(f'{b} is less than {a}')
# elif b == a:
#     print(f'{b} is equal to {a}')
# else:
#     print('Nothing will happen')

# x = int(input('Enter any First number: '))
# y = int(input('Enter any Second number: '))
# z = int(input('Enter any Third number: '))

# if y > x:
#     if z > y:
#         print(z, 'is greater')
#     else:
#         print(y, 'is greater')
# else:
#     if z > x:
#         print(z, 'is greater')
#     else:
#         print(x, 'is greater')
# print("Done")

# LOOP

a = [1,2,3,4,5,10]
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])

# for i in a:
#     print(i)
fruits = ['banana','apple','cherry']
# for x in fruits:
#     if x == 'apple':
#         break
#     print(x)

# for x in fruits:
#     if x == 'apple':
#         pass
#     print(x)

# for i in range(6):
#     print(i)
# else:
#     print("Finally finished")

a = ['red', 'big', 'small']
# fruits = ['banana','apple','cherry']

# for x in a:
#     for y in fruits:
#         print(x, y)



    
    

# count = int(input('How many times do you want to say "Hello": '))

# i = 1

# while i <= count:
#     print('Hello')
#     i += 1
# print('Job is Done! Thank You!')

# i = 1

# while i < 6:
#     print(i)
#     if i == 4:
#         break
#     i += 1

# Function
# def name(arg1, arg2,... argN):
#     statements

def my_function():
    print("Hello From a function")

# my_function()

def name(fname):
    print(fname + " Caleb")

# name("Caleb")

# def area_of_circle(PI=3.142, r=float(input("Enter the radius: "))):
#     PI=PI
#     r = r
#     area = PI * r**2
#     print("The Area of the Circle is: ", area)

# area_of_circle()
my_list = [1,'cat',0.5]
# print(my_list)

def add_list(my_list):
    my_list.append([1,'cat',0.5])
    # print("Value inside the Function: ", my_list)
    return

# my_list = [10,20,30]
# add_list(my_list)
# print("Value Outside the Function: ", my_list)

def mul_five(x):
    return 5 * x

# print(mul_five(5))
# print(mul_five(2))
# print(mul_five(4))
# print(mul_five(3))


def test(k):
    if (k > 0):
        result = k + test(k-1)
        print(result)
    else:
        result = 0
    return result

# test(6)

def greet(name):
    print("Hello, "+ name + ". Good morning")

# greet('Caleb')

def convert(text):
    x = text.upper()
    print(x)

# text = input('Enter String. ')
# convert(text)

def to_uppercase():
    text = input('Enter the lowercase string: ')
    uppercase = text.upper()
    print(uppercase)

# to_uppercase()

def count(val):
    con=0 
    vov=0
    for i in range(len(val)):
        if val[i] in ['a','e','i','o','u']:
            vov = vov+1
        else:
            con = con+1

    print("The Count of Vowel is", vov)
    print("The Count of Consonant is", con) 
    

x = input('Enter any word: ')
count(x)

