text_path = 'random.txt'

'''
# Handle a file using open(), read() and close() functions
simple_text = open(text_path, 'r')
text = simple_text.read()
print(text)
simple_text.close()
'''

''' 
# Handle a file using a context manager: with statement automatically closes the file when done
with open(text_path, 'r') as f:
    text = f.read()
    print(text)
'''

''' 
# 'r' is for reading files, 'a' is for appending to the end of files. \n creates a new line
with open(text_path, 'a') as f:
    f.write('\nThis is a new line.')
'''

''' 
# readlines() stores each line of text as an item in a list
with open(text_path, 'r') as f:
    text = f.readlines()
    print(text)
'''

''' 
# 'x' is for creating new files
try:
    with open('another_file.txt', 'x') as f:
        f.write('This is another new file')
        print('File created')
except FileExistsError as e:
    print("Sorry, 'another_file.txt' already exists")
'''

# 'w' checks if the file exists. If it exists, 'w' overwrites it. If not, 'w' creates a new file
with open('another_random_file.txt', 'w') as f:
    f.write("Hello, from keyword 'w'\nThis is a takeover!")
    print('Done creating or overwiting')