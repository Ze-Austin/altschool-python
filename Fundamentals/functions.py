# Function that greets the user in the terminal
def greet_user():
    user = str(input("What's your name? "))
    print(f'Hello {user}')
# greet_user()

# Function to calculate and print the area of a circle
def circle_area():
    PI = 3.142
    r = float(input('Enter the circle radius in metres: '))
    area = PI * r ** 2
    print(f'The area of this circle is {area}m2')
    return area
# circle_area()

# Recursive Function
def test(k):
    if (k > 0):
        result = k + test(k - 1)
        print(result)
    else:
        result = 0
    return result
# test(5)

# Print Name & Age
def user_details(name, age):
    print(f"Name: {name}. Age: {age}")
# user_details('Austin', 27)

# Convert Input to Uppercase
def to_uppercase():
    text = input('Enter the lowercase string: ')
    uppercase = text.upper()
    print(uppercase)
# to_uppercase()

# Count vowels and consonants in a string
def vowels_vs_consonants():
    original_text = input('Enter the string: ')
    lower_text = original_text.lower()
    vowel_count = 0
    cons_count = 0
    for i in range(len(lower_text)):
        if lower_text[i] in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
        elif lower_text[i] in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']:
            cons_count += 1
        else:
            continue
    print(f'There are {vowel_count} vowel(s) and {cons_count} consonant(s) in "{original_text}".')
# vowels_vs_consonants()

# Factorial
def factorial():
    original_num = int(input('Enter an Integer: '))
    num = original_num
    fact = 1
    while num != 0:
        fact *= num
        num -= 1
    print(f"{original_num}! = {fact}")
    return fact
# factorial()
