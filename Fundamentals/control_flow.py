''' 
# ELIF Stetements
x = int(input('Enter First Number: '))
y = int(input('Enter Second Number: '))

if x > y:
    print(f'{x} is greater than {y}')
elif y > x:
    print(f'{y} is greater than {x}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print('Nothing happens')
'''

'''
# Nested IF Statements
a = int(input('Enter First Number: '))
b = int(input('Enter Second Number: '))
c = int(input('Enter Third Number: '))

if b > a:
    if c > b:
        print(c, 'is the greatest')
    else:
        print(b, 'is the greatest')
else:
    if c > a:
        print(c, 'is the greatest')
    else:
        print(a, 'is the greatest')
print('Done')
'''

''' Iterative Statements '''
list_of_names = ['John', 'Jane', 'Jack', 'Jill']

'''
# For Loop
for name in list_of_names:
    print(f'Hello {name}!') 
'''

''' 
# For Loop with a generator function: range() stops at the number BEFORE the end
# range() with only one number within the parentheses will start from 0 and end before the number

for i in range(1, 10):
    print(i)
'''

'''
# While Loop
i = 0
while i < len(list_of_names):
    print(f'Hello {list_of_names[i]}!')
    i += 1
print(f'Job is done. Thank you!')
'''

''' Transfer Statements: Break, Continue & Pass '''

''' 
# Pass tells the compiler to do nothing
def print_list(list_of_names):
    pass
'''

'''
# Break ends the loop at that step, without doing the step
# Continue skips the current step of the loop

list_comprehensions = [i for i in range(1, 11)]
# print(list_comprehensions)

list_comprehensions.append(0)
list_comprehensions.append(12)
print(list_comprehensions)

for number in list_comprehensions:
    if number == 0:
        break
    if number % 2 != 0:
        continue
    print(number)
'''
