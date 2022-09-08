''' Lists: mutable, ordered collection of items. Created with square brackets [] '''
empty_list = []
# print(empty_list)

list1 = [1, 'food', 2.5, 'drink', 49]
# print(list1[1])
# print(f'The item at index 1 is {list1[1]}')

list1.append(35)
# print(list1)

list1.pop()
# print(list1)

# List length
# print(len(list1))

# Slicing lists
# print(list1[1:4])
# print(list1[1:])
# print(list1[2:-1])

# Find an item in a list
# print(list1.index('drink'))

# Modify an item in a list
list1[1] = 'rice'
# print(list1)

# Healthy examples
fruit_basket = ['apple', 'banana', 'orange']
fruit_basket.append('grape')
# print(fruit_basket)
# fruit_basket.remove('apple')
# print(fruit_basket)
# fruit_basket.pop(2)
# print(fruit_basket)


# Concatenate lists
vegetable_basket = ['tomato', 'potato', 'carrot']
mixed_basket = fruit_basket + vegetable_basket
# print(mixed_basket)

# Count occurences of an item in a list
# print(mixed_basket.count('carrot'))

''' In-built Functions for Lists in Python '''
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum(num_list))
# print(min(num_list))
# print(max(num_list))

''' Boolean: Zero is False; Every other number is True '''
zero_int = 0
# print(bool(zero_int))
# print(not zero_int)

''' Dictionaries: created with curly braces {}. Keys are Case-Sensitive '''
empty_dict = {}
# print(empty_dict)

name_dict = {1: 'Jenny', 2: 'Mike', 3: 'Ahmed'}
# print(name_dict[1])

food_dict = {
    'Nigerian': ['eba', 'jollof rice', 'fufu', 'yam porridge'],
    'Italian': ['spaghetti', 'macaroni', 'pizza', 'mozzarella']
}
# print(food_dict['Italian'])
# print(food_dict['Nigerian'][1])
# print(food_dict['Italian'][-1])
# print(food_dict['Nigerian'][0:-1])

age_dict = {'Ada': 10, 'Caleb': 12}
# print(age_dict['Caleb'])

# Add a new key-value pair to a dictionary
age_dict['Peter'] = 40
# print(age_dict)

# Get the value of a key in the dictionary
# print(age_dict.get('Ada'))

''' dictionary.pop() must have an argument key passed into the bracket '''
age_dict.pop('Peter')
# print(age_dict)

# Clear the whole dictionary and return empty dictionary
# age_dict.clear()
# print(age_dict)

# Delete a key-value pair in the dictionary
# del age_dict['Caleb']
# print(age_dict)


''' Merging Dictionaries: the combined dictionary will update any duplicate keys to only the latest value '''
second_dict = {'Austin': 27, 'Michel': 30, 'Ada': 32}

# Copy method
# new_dict = age_dict.copy()
# new_dict.update(second_dict)
# print(new_dict)

# Standard method
new_dict = {**age_dict, **second_dict}
# print(new_dict)# Dictionary length
# print(len(new_dict))

# Check if a key exists in a dictionary
# print('Austin' in new_dict)
# print('Eli' in new_dict)

# Get all Keys, Values and Items in a dictionary
# print(new_dict.keys())
# print(new_dict.values())
# print(new_dict.items())

''' dictionary.items() stores the items in a list of tuples, so it's possible to then iterate over them '''

# Nested Dictionaries
school_dict = {
    'class': {
        'student': {
            'name': 'Chinedu',
            'scores': {
                'math': 88,
                'history': 79
            }
        }
    }
}

# print(school_dict['class']['student']['scores']['history'])

''' Tuples: immutable lists, created using tuple(()) or brackets and at least 1 item & 1 comma: (item,) '''
t_var = (3,)
# print(type(t_var))

simple_tuple = tuple((1, 2, 3, 4, 5, 6))
# print(type(simple_tuple))
# print(simple_tuple)


# Packing and Unpacking Tuples
sample_tuple = ('John', 25, 'Doe')
first_name, age, last_name = sample_tuple
# print(last_name)

# Accessing items in a tuple
# print(sample_tuple[0])
# print(sample_tuple[-3])

# Slicing a tuple
# print(simple_tuple[1:5])

# Get the index of an item in a tuple
# print(sample_tuple.index('Doe'))

''' You can change an item in a list within a tuple, but not the tuple items themselve '''
# Modifying an item in a tuple will return an error
# sample_tuple[1] = 30
# print(sample_tuple)

# Modifying an item in a nested list within a tuple will work
fun_tuple = ('p', 'y', 't', 'h', 'o', 'n', [1, 2, 3])
# print(fun_tuple[-1][1])
fun_tuple[-1][2] = 50
# print(fun_tuple[-1])

''' Converting Tuples and Lists back and forth '''
tuple_to_list = list(fun_tuple)
# print(type(tuple_to_list))

list_to_tuple = tuple(tuple_to_list)
# print(type(list_to_tuple))

# Count occurences of an item in a tuple
# print(fun_tuple.count('o'))

# In-Built functions for Tuples
# print(sum(simple_tuple))
# print(min(simple_tuple))
# print(max(simple_tuple))

''' Sets: creeated with curly braces {} or set([]), but no key-value pairs. Items within sets are unique, with no duplicates allowed '''
sample_set = {'Mark', 'Jessica', 20, 33}
# print(type(sample_set))

another_set = set(['Hello', 'World', 2022])
# print(type(another_set))

''' Convert List to Set: new set is ordered and duplicates are dropped '''
number_list = [1, 4, 5, 9, 1, 5, 3, 7]
# print(len(number_list))

number_set = set(number_list)
# print(len(number_set))
# print(number_set)

# Check if an element is in a set
# print(8 in number_set)

# Add non-duplicate item to a set
number_set.add(11)
# print(number_set)

''' Remove an item from a set: remove() throws an error if the item is initially absent, while discard() does not throw an error if the item was not there '''
number_set.remove(3)
# print(number_set)
number_set.discard(10)
# print(number_set)

# Set Operations
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}

''' Union of two sets: pipe symbol | or .union() '''
all_colors = color_set | remaining_colors
# all_colors = color_set.union(remaining_colors)
# print(all_colors)

''' Intersection between sets: ampersand & or .intersection() '''
color_intersect = color_set & remaining_colors
# color_intersect = color_set.intersection(remaining_colors)
# print(color_intersect)

''' Difference between sets: minus sign - or .difference() '''
color_difference1 = color_set - remaining_colors
# print(color_difference1)

color_difference2 = remaining_colors.difference(color_set)
# print(color_difference2)

''' Symmetric difference: items in both sets, excluding all intersecting items. Uses caret sign ^ or .symmetric_difference() '''
color_sym_diff = color_set ^ remaining_colors
# color_sym_diff = color_set.symmetric_difference(remaining_colors)
# print(color_sym_diff)

''' Check if a set is a subset of another with issubset(), superset with isssuperset() '''
new_colors = {'violet', 'blue', 'yellow'}
# print(new_colors.issubset(color_set))
# print(remaining_colors.issubset(color_set))
# print(color_set.issuperset(new_colors))

''' Sorting a set will convert it to a list, but the new sorted list can be converted back to a set '''
num_set = {4, 6, 9, 2, 5, 1, 3, 8, 7, 10}
# sorted_list = sorted(num_set)
# sorted_set = set(sorted_list)
sorted_set = set(sorted(num_set))
# print(sorted_set)