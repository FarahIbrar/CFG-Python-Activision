#!/usr/bin/env python
# coding: utf-8

# ### Starter: There are four mistakes in this program. What are the mistakes and how would you fix them?
# 
# ``` Python 
# carrots = input('How many carrots do you have? ')
# rabbits = 6
# if rabbits < carrots:
#     print('There are not enough carrots')
# if rabbits > carrots:
#     print('There are too many carrots')
# else:
#     print('You have the right number of carrots')
# ```

# - **Indentation Error:** The print statements within the if and else blocks need to be properly indented.
# - **Type Error:** The input function returns a string, so we need to convert the input to an integer to perform numerical comparisons.
# - **Logical Error:** The conditions for checking if there are not enough carrots and too many carrots are incorrect.
# - **Redundant Condition:** The second condition if rabbits > carrots: is redundant since it can be replaced with else.

# In[2]:


carrots = int(input('How many carrots do you have? '))
rabbits = 6
if rabbits > carrots:
    print('There are not enough carrots')
elif rabbits < carrots:
    print('There are too many carrots')
else:
    print('You have the right number of carrots')


# ### Explanation of Fixes:
# 
# 1. **Indentation**: The `print` statements are now properly indented to align with the if, elif, and else statements.
# 2. **Type Conversion**: The input for `carrots` is converted to an integer using `int()`.
# 3. **Logical Error Fix**: The comparison logic is updated. If `rabbits > carrots`, it means there are not enough carrots. If `rabbits < carrots`, it means there are too many carrots.
# 4. **Redundant Condition Fix**: The second condition is replaced with `elif` to handle the case when `rabbits < carrots`. The `else` now correctly handles the case when the number of rabbits equals the number of carrots.

# In[ ]:





# ## This session:
# 
# 1. Lists
# 2. Dictionaries

# ## Lists:

# **List:** an ordered collection of values

# - List are written inside square brackets and separated by commas

# In[4]:


# A list of integers
lottery_numbers = [4, 8, 15, 16, 23, 42]
lottery_numbers


# In[3]:


#A list of strings
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
student_names


# - Lists can be made up of values of one or more data types
# 
# ```Python
# person = ['Jess', 32]
# ```

# In[5]:


person = ['Jess', 32]
person


# - List values can be accessed using their **index** in square brackets

# In[5]:


student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
print(student_names[2])


# - List indexes start counting from 0

# In[8]:


student_names = [
    'Diedre', # index 0
    'Hank', # index 1
    'Helena', # index 2
    'Salome' # index 3
]
    
print(student_names[0])


# You can also set the values in lists using their indexes, similar to how you would set a variable

# In[9]:


student_names = [
    'Diedre', # index 0
    'Hank', # index 1
    'Helena', # index 2
    'Salome' # index 3
]

student_names[1] = 'Joshua'

print(student_names)


# In[ ]:





# ### Exercise 4.1: When I'm travelling in the winter I often forget to pack warm clothes. Let's write a program to help me to remember the right clothes.
# 
# The program should check if the first item in the clothes list is `"shorts"` . If it is it should change the value to `"warm coat"`.

# In[6]:


clothes = [
    "shorts",
    "shoes",
    "t-shirt",
]
clothes


# In[11]:


# Define the initial clothes list
clothes = [
    "shorts", 
    "t-shirt", 
    "hat", 
    "gloves"
]

# Check if the first item is "shorts" and replace it with "warm coat" if true
if clothes[0] == "shorts":
    clothes[0] = "warm coat"

# Print the updated clothes list
print("Updated clothes list:", clothes)


# In[ ]:





# ## List Functions:

# There are functions designed for lists
# 
# - **len( ):** the number of items in a list
# - **max( ):** The biggest value in a list
# - **min( ):** The smallest value in a list

# In[12]:


costs = [1.2, 4.3, 2.0, 0.5]

print(len(costs))
print(max(costs))
print(min(costs))


# Functions for changing the order of a list
# 
# - **sorted( ):** Sorts the
# = **reversed( ):** Reverses the order of a list

# In[13]:


costs = [1.2, 4.3, 2.0, 0.5]

print(sorted(costs))
print(list(reversed(costs)))


# In[ ]:





# ### Exercise 4.2: Make a list of game scores. Using list functions write code to output information of the scores in the following format:
# 
# - Number of scores: 10
# - Highest score: 200
# - Lowest score: 3
#     
# **Extension:** Output all of the scores in descending order

# In[15]:


# Define the list of game scores
scores = [75, 120, 50, 3, 90, 200, 35, 80, 10, 150]

# Output the number of scores
print(f"Number of scores: {len(scores)}")

# Output the highest score
print(f"Highest score: {max(scores)}")

# Output the lowest score
print(f"Lowest score: {min(scores)}")

# Output all scores in descending order
sorted_scores = sorted(scores, reverse=True)
print("Scores in descending order:")
for score in sorted_scores:
    print(score)


# BOTH CODES SHOW SAME RESULTS!!!

# In[16]:


# List of game scores
scores = [50, 120, 80, 3, 150, 200, 90, 30, 10, 5]

# Number of scores
num_scores = len(scores)

# Highest score
highest_score = max(scores)

# Lowest score
lowest_score = min(scores)

# Output information
print('Total number of scores: {}'.format(num_scores))
print('Highest score achieved: {}'.format(highest_score))
print('Lowest score achieved: {}'.format(lowest_score))

# Extension: Output all scores in descending order
sorted_scores = sorted(scores, reverse=True)
print('Scores in descending order:', sorted_scores)


# In[ ]:


scores = [50, 120, 80, 3, 150, 200, 90, 30, 10, 5]

num_scores = len(scores)

highest_score = max(scores)

lowest_score = min(scores)

print('Total number of scores: {}'.format(num_scores))
print('Highest score achieved: {}'.format(highest_score))
print('Lowest score achieved: {}'.format(lowest_score))

sorted_scores = sorted(scores, reverse=True)
print('descending order scores:', sorted_scores)


# In[ ]:





# ## append ( ) and in:

# You can check if an value is `in` a list using the in operator. 
# 
# If the value is in the list it will result in `True` and `False` if it is not.

# In[17]:


student_name = input('Which student are you looking for? ')

students = [
'Diedre', 'Hank', 'Helena', 'Salome',
]

if student_name in students:
    print('{} is in the class'.format(student_name))
else:
    print('{} is not in the class'.format(student_name))


# The `.append()` method is used to add items to a list

# In[19]:


students = [
'Diedre', 'Hank', 'Helena', 'Salome',
]

student_name = input('What is the name of the new student? ')

students.append(student_name)

print(students)


# In[ ]:





# ### Exercise 4.3: Whenever I'm shopping and I buy some bread I always forget to buy butter. Create a list and if 'bread' is in the list, add 'butter' to the shopping list.
# 
# Try running the program with and without bread in the list to check that your program works.
# 
# Remember the in operator checks if an item is in a list and the .append() method adds an item to a
# list.

# In[22]:


shopping_list = ['milk', 'eggs', 'cheese']

if 'bread' in shopping_list:
    print('Great! Bread is in the list.')
else:
    print('Oh No! You forgot to add the Bread.')


# In[24]:


shopping_list = ['milk', 'eggs', 'cheese']

if 'bread' in shopping_list:
    print('Great! Bread is in the list.')
elif 'bread' not in shopping_list:
    print('Oh No! You forgot to add the Bread.')
    
    shopping_list.append('butter')
    print('Butter is in the list now!')

# Output the updated shopping list
print('New shopping list:', shopping_list)


# In[ ]:





# In[4]:


shopping_list = [
    'Bread',
    'cheese',
    'pop tarts',
    'carrots',
]

if 'bread' in shopping_list:
    shopping_list.append('butter')
    
print (shopping_list)

#Example for case sensitive


# In[ ]:





# To check if an item is `not` in a `list`

# In[25]:


fridge = [
    'cheese',
    'pizza',
    'coke',
]

if 'milk' not in fridge:
    print('You have no milk in the fridge')


# In[ ]:





# ## For Loops ♥ Lists:

# Using lists and for loops together

# In[1]:


student_names = ['Diedre', 'Hank', 'Helena', 'Salome']

for student_name in student_names:
     print(student_name)


# Counting the total number of items in a list using a for loop

# In[2]:


student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
count = 0

for student_name in student_names:
    count = count + 1
    
print(count)


# In[ ]:





# ### Exercise 4.4: I want to work out how much money I've spent on lunch this week. I've created a list of what I spent each day.
# - Write a program that uses a for loop to calculate the total cost

# In[8]:


daily_coffee_expenses = [3.25, 4.50, 3.75, 4.00, 5.25]

total_expense = 0

for cost in daily_coffee_expenses:
    total_expense += cost

print("Total expense for coffee for the week: £", total_expense)


# In[13]:


daily_coffee_expenses = [3.25, 4.50, 3.75, 4.00, 5.25]

total_expense = 0

for cost in daily_coffee_expenses:
    total_expense = total_expense + cost

print("Total expense for coffee for the week: £", total_expense)


# In[ ]:





# In[15]:


daily_coffee_expenses = [3.25, 4.50, 3.75, 4.00, 5.25]

total_expense = daily_coffee_expenses[0]

for cost in daily_coffee_expenses[1:]:
    total_expense = total_expense + cost

print("Total expense for coffee for the week: £", total_expense)


# In[ ]:





# - There is an easier way to do the last program without a for loop. 
# - The **sum( )** function can be used to add up all of the values in a list:

# In[14]:


costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total = sum(costs)

print(total)


# In[ ]:





# ## Dictionaries

# **Dictionary:** Stores a colleciton of labelled items. Each item has a `key` and a `value`.

# In[16]:


person = {
    'name': 'Jessica',
    'age': 23,
    'height': 172
}


# Values in a dictionary are accessed using their keys.

# In[17]:


person = {
    'name': 'Jessica',
    'age': 23,
    'height': 172
}

print(person['name'])


# In[ ]:





# ### Exercise 4.5: Print the values of name , post_code and street_number from the dictionary
# - Extension: Print the values of longitude and latitude from the inner dictionary.

# In[18]:


person = {
    'full_name': 'Alice Smith',
    'postal_code': '54321',
    'house_number': '789',
    'coordinates': {
        'longitude': 12.345,
        'latitude': -45.678
    }
}


print("Full Name:", person['full_name'])
print("Postal Code:", person['postal_code'])
print("House Number:", person['house_number'])

print("Longitude:", person['coordinates']['longitude'])
print("Latitude:", person['coordinates']['latitude'])


# In[ ]:





# ## Dictionaries in Lists:

# Putting dictionaries inside a list is very common.

# In[19]:


people = [
    {'name': 'Jessica', 'age': 23},
    {'name': 'Trisha', 'age': 24},
]

for person in people:
    print(person['name'])
    print(person['age'])


# In[ ]:





# ### Exercise 4.6: Using a for loop, output the values name , colour and price of each dictionary in the list

# In[20]:


products = [
    {"name": "Chair", "colour": "Red", "price": 49.99},
    {"name": "Desk", "colour": "Brown", "price": 129.99},
    {"name": "Lamp", "colour": "Silver", "price": 19.99}
]

for product in products:
    print(product['name'] + " - Colour: " + product['colour'] + ", Price: $" + str(product['price']))


# In[22]:


electronics = [
    {"name": "Smartphone", "brand": "Samsung", "price": 799.99},
    {"name": "Laptop", "brand": "Dell", "price": 1299.99},
    {"name": "Tablet", "brand": "Apple", "price": 599.99}
]


for item in electronics:
    print(item['name'] + " by " + item['brand'] + " - Price: $" + str(item['price']))


# In[21]:


# List of dictionaries
products = [
    {"name": "Chair", "colour": "Red", "price": 49.99},
    {"name": "Desk", "colour": "Brown", "price": 129.99},
    {"name": "Lamp", "colour": "Silver", "price": 19.99}
]

# Iterating through the list and printing values
for product in products:
    print(f"{product['name']} - Colour: {product['colour']}, Price: ${product['price']}")


# In[ ]:





# ## Random Choice:

# The choice( ) function in the random module returns a random item from a list

# In[23]:


import random

colours = ['red', 'green', 'blue']
chosen_colour = random.choice(colours)

print(chosen_colour)


# In[ ]:





# ### Exercise 4.7: Write a program to create a random name. You should have a list of random first names and a list of lastnames. Choose a random item from each and display the result.
# 
#     Extension: Using list of verbs and a list of nouns, create randomised sentences

# In[24]:


import random

# Lists of random first names and last names
first_names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Sarah']
last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis']

# Lists of random verbs and nouns for sentences
verbs = ['runs', 'jumps', 'plays', 'eats', 'sleeps', 'reads']
nouns = ['ball', 'dog', 'cat', 'book', 'tree', 'house']

# Function to generate a random name
def generate_random_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f'{first_name} {last_name}'

# Function to generate a random sentence
def generate_random_sentence():
    subject = random.choice(first_names)
    verb = random.choice(verbs)
    object = random.choice(nouns)
    return f'{subject} {verb} the {object}.'

# Generating and printing a random name
random_name = generate_random_name()
print("Random Name:", random_name)

# Generating and printing a random sentence
random_sentence = generate_random_sentence()
print("Random Sentence:", random_sentence)


# In[25]:


import random

# Lists of unique first names and last names
first_names = ['Ella', 'Liam', 'Ava', 'Noah', 'Olivia', 'James']
last_names = ['Anderson', 'Wilson', 'Miller', 'Taylor', 'Clark', 'Moore']

# Lists of random verbs and nouns for sentences
verbs = ['runs', 'jumps', 'paints', 'eats', 'sleeps', 'reads']
nouns = ['ball', 'dog', 'cat', 'book', 'tree', 'house']

# Function to generate a random name
def generate_random_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f'{first_name} {last_name}'

# Function to generate a random sentence
def generate_random_sentence():
    subject = random.choice(first_names)
    verb = random.choice(verbs)
    object = random.choice(nouns)
    return f'{subject} {verb} with the {object}.'

# Generating and printing a random name
random_name = generate_random_name()
print("Generated Name:", random_name)

# Generating and printing a random sentence
random_sentence = generate_random_sentence()
print("Generated Sentence:", random_sentence)


# In[ ]:





# ## Recap:

# This session:
# 1. Lists
# 2. Dictionaries

# ### Question 1: What shape brackets are used for creating a list and what shape brackets are used for creating a dictionary?
# 
# - **Lists** in Python are created using **square brackets**: `[]`.
#   - Example: `my_list = [1, 2, 3]`
# - **Dictionaries** in Python are created using **curly brackets**: `{}`.
#   - Example: `my_dict = {'key': 'value'}`
# 
# ### Question 2: What is the result of this program?
# ```python
# cheeses = [
#     'brie',
#     'cheddar',
#     'wensleydale',
#     'edam',
# ]
# print(cheeses[4])
# ```
# 
# **Result**:
# - The list `cheeses` has 4 elements indexed from `0` to `3` (`cheeses[0]` is `'brie'`, and `cheeses[3]` is `'edam'`).
# - The program attempts to access `cheeses[4]`, which is out of bounds because there is no element at index `4`.
# - **This will raise an `IndexError`:** `list index out of range`.
# 
# ### Question 3: This program raises an error when I run it. What do I need to change to get it to run?
# 
# Here’s the original program:
# 
# ```python
# trees = [
#     {'leaf_colour': 'green', 'height': 2120},
#     {'leaf_colour': 'green', 'height': 2300},
# new_tree = {
#     'leaf_colour': 'green',
#     'height': 1020
# }
# trees.append(new_tree)
# print(trees)
# ```
# 
# **Error Explanation**:
# - The error is a `SyntaxError` caused by a missing closing square bracket `]` for the list `trees`.
# 
# **Corrected Code**:
# ```python
# trees = [
#     {'leaf_colour': 'green', 'height': 2120},
#     {'leaf_colour': 'green', 'height': 2300},
# ]  # Closing square bracket added here
# new_tree = {
#     'leaf_colour': 'green',
#     'height': 1020
# }
# trees.append(new_tree)
# print(trees)
# ```
# 
# **Summary of Corrections**:
# 1. **Add a closing square bracket** `]` after the second dictionary in the list `trees`.
# 
# After making this change, the code will run without errors and will correctly append `new_tree` to the `trees` list, then print the updated list.

# In[7]:


# Question 2 (wrong version):
cheeses = [
    'brie',
    'cheddar',
    'wensleydale',
    'edam',
]
print(cheeses[4])


# In[10]:


# Question 2 (correct version):
cheeses = [
    'brie',
    'cheddar',
    'wensleydale',
    'edam',
]
print(cheeses[3])  # Changed the index from 4 to 3


# ### Corrected Version for Question 2
# 
# To fix the `IndexError` in Question 2, you need to access a valid index within the bounds of the `cheeses` list. Since the list `cheeses` has indices ranging from `0` to `3`, you can choose any of these indices to avoid the error.
# 
# Here’s the corrected version of the program:
# 
# ```python
# cheeses = [
#     'brie',
#     'cheddar',
#     'wensleydale',
#     'edam',
# ]
# print(cheeses[3])  # Changed the index from 4 to 3
# ```
# 
# This code will output:
# ```
# edam
# ```
# 
# By using `cheeses[3]` instead of `cheeses[4]`, you access a valid index and prevent the `IndexError`.

# In[8]:


# Question 3 (wrong version):
trees = [
    {'leaf_colour': 'green', 'height': 2120},
    {'leaf_colour': 'green', 'height': 2300},
new_tree = {
    'leaf_colour': 'green',
    'height': 1020
}
trees.append(new_tree)
print(trees)


# In[9]:


# Question 3 (correct version):
trees = [
    {'leaf_colour': 'green', 'height': 2120},
    {'leaf_colour': 'green', 'height': 2300},
]  # Closing square bracket added here
new_tree = {
    'leaf_colour': 'green',
    'height': 1020
}
trees.append(new_tree)
print(trees)


# In[ ]:




