# Statements in Python
# site = 'gfg'

# integer = 1, 2, 3, 4, 5, 500
# strings = 'caleb', 'orange'
# floats = 0.1, 33.5, 44.0, 14.4
# boolean = True, False

# # all_list = [2, 3, 4, 5, 'caleb', 'apple', True, False, 0.1, 0.5]

# # print(all_list)

# # Area of a circle
# # PI = 3.142  #creating my PI

# # r = float(input("Enter the radius: ")) # Inputing my radius

# # area_of_circle = PI * r**2 # Calculating the area of a circle

# # print("The Area of the Circle is: ", area_of_circle)  #  Printing the result


# # var1 = 1
# # var_1 = 1
# # var 1 =1

# # VAR = 3.143



# list1 = ["abc", 34, True, 40, "male", 0.5]
# print(list1)

# list1.append(35)
# print(list1)

# list1.pop(3)
# print(list1)


# print(list1[0:5])

# # List

# fruits=['apples','oranges','bananas','mangoes','grapes','strawberry']
# print(fruits[1])

''' 
if site == 'gfg':
    print('Logging on to geeksforgeeks...')
else:
    print('retype the URL.')
print('All set !')
'''
# Boolean
# a = 1>2
# print(a)

# zero_int = 0

# print(bool(zero_int))

#Boolean Arithmetic
# or
# and
# not
# ==(eqivalent)
# !=(not eqivalent)

# A = True
# B = False
# C = False

# print(A or B)
# print(not A)
# print(A == B)
# print(A != B)
# print(A or (C and B))
# print((A and B) or C)


# Dictionaries
# age_dict = {"Ada": 10, "Caleb": 12, "John": 12}
# print(age_dict)
# age_dict["Peter"] = 40
# print(age_dict)
# age_dict.pop("John")
# print(age_dict)

# my_dict = {"name":"John", "age":26, "Ada": 10, "Caleb": 12, "John": 12}
# print(my_dict['name'])
# print(my_dict.get('age'))
# print(my_dict.pop("John"))
# my_dict.clear()
# print(my_dict)

# dict1 = {'Ten':10, 'Twenty':20}
# dict2 = {'Fifty':50, 'Thirty':30}
# dict3 = dict1.copy()

# dict3.update(dict2)

# dict3 = {**dict1, **dict2}
# print(dict3)

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics":70,
#                 "history":80,
#             }
#         }
#     }
# }

# print(sampleDict['class'])
# print(sampleDict['class']['student'])
# print(sampleDict['class']['student']['marks'])
# print(sampleDict['class']['student']['marks']['history'])

# sampleDict = {
#     'emp1': {'name':'John', 'salary':7000},
#     'emp2': {'name':'Emma', 'salary':8000},
#     'emp3': {'name':'Amaka', 'salary':9000}
# }
# print(sampleDict)
# sampleDict['emp3']['salary'] = 6000
# print(sampleDict)

# Tuple
# t_var = (3, 4, 5, 6, 10, 20, 8)
# print(t_var[-2:])

# tuple1 = (11, [22, 33], 44, 55)
# print(tuple1)
# tuple1[1][0] = 222
# print(type(tuple1))

# tuple1 = (11, 22, 33, 44, 55)
# tuple1[1] = 222
# print(tuple1)

# Set
# sameple_set = {'Mark', 'Jessa', 45, 50}
# print(type(sameple_set))

# sameple_set = set(('Mark', 'Jessa', 45, 50))
# print(type(sameple_set))

# list1 = [20, 30, 40, 50]
# print(type(list1))
# list1 = set(list1)
# print(type(list1))

a = {2,4,6,8,10}
b = {1,3,5,7,9,2,4}

# c = a | b
# print(c)

c = a.union(b)
print(c)

# c = a & b
# c = a.intersection(b)
# print(c)

# c = a - b
# print(c)
