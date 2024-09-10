#!/usr/bin/env python
# coding: utf-8

# # Week 5 - python session

# #### Starter: How do I output the species values for each of the dictionaries?
# ```Python
# [
#      {'species': 'zebra', 'name': 'Penelope'},
#      {'species': 'penguin', 'name': 'Jenn'},
#      {'species': 'elephant', 'name': 'Harris'},
#      {'species': 'flamingo', 'name': 'Florence'},
# ]
# ```

# To output the species values for each of the dictionaries in the list, you can iterate through the list and access the value associated with the `species` key for each dictionary.
# 
# Here's how to do this:

# In[1]:


animals = [
    {'species': 'zebra', 'name': 'Penelope'},
    {'species': 'penguin', 'name': 'Jenn'},
    {'species': 'elephant', 'name': 'Harris'},
    {'species': 'flamingo', 'name': 'Florence'},
]

# Iterate through each dictionary in the list
for animal in animals:
    # Print the value associated with the 'species' key
    print(animal['species'])


# In[ ]:





# This session
# 
# 1. Files
# 2. Pip package manager
# 3. APIs

# In[ ]:





# ## Reading/Writing Files:

# In[2]:


people = 'Farah\nMisbah\nMaryam\nUmar'

file_path = '/Users/farah/Desktop/people.txt'

with open(file_path, 'w+') as text_file:
    text_file.write(people)


# ## Reading from a file:

# In[4]:


with open(file_path, 'r') as text_file:
    contents = text_file.read()

print(contents)


# In[ ]:





# ### Exercise 5.1: Create a to-do list program that writes user input to a file
# 
# The program should:
# - Ask the user to input a new to-do item
# - Read the contents of the existing to-do items
# - Add the new to do item to the existing to-do items
# - Save the updated to-do items
# 
# You will need to manually create a new list called `todo.txt` in the same folder as your program before you start.

# In[1]:


new_item = input('Enter a to-do item: ') 

with open('todo.txt', 'r') as todo_file:
    todo = todo_file.read()

todo = todo + new_item + '\n'

with open('todo.txt', 'w+') as todo_file: todo_file.write(todo)


# This is an improved version of the code that handles potential errors and simplifies the file operations:
# 
# ```python
# # Ask the user for a new to-do item
# new_item = input('Enter a to-do item: ')  
# 
# # Append the new to-do item directly to the file
# try:
#     with open('todo.txt', 'a') as todo_file:  # Open the file in append mode
#         todo_file.write(new_item + '\n')  # Write the new item to the file with a newline character
#     print("To-do item added successfully!")
# except FileNotFoundError:
#     print("The file 'todo.txt' was not found. Please make sure it exists.")
# ```
# 
# #### Changes Made and Reasons:
# 
# 1. **Using `'a'` (Append) Mode:**
#    - **What Changed:** Switched from reading (`'r'`) and writing (`'w'`) to just using append mode (`'a'`).
#    - **Why:** The `'a'` mode allows you to directly add a new item to the end of the file without reading the entire file first. This is more efficient because it avoids unnecessary file I/O operations, making the code simpler and faster.
# 
# 2. **Error Handling with `try-except`:**
#    - **What Changed:** Added a `try-except` block to handle cases where the file `todo.txt` might not exist.
#    - **Why:** If `todo.txt` does not exist, trying to open it would raise a `FileNotFoundError`. The `try-except` block gracefully handles this scenario by informing the user and preventing the program from crashing.
# 
# 3. **User Feedback:**
#    - **What Changed:** Added a `print` statement to confirm that the to-do item was added successfully.
#    - **Why:** Providing feedback to the user enhances the user experience by confirming that their action was successful.
# 
# These changes make the code more robust, efficient, and user-friendly.

# In[ ]:


# Ask the user for a new to-do item
new_item = input('Enter a to-do item: ')  

# Append the new to-do item directly to the file
try:
    with open('todo.txt', 'a') as todo_file:  # Open the file in append mode
        todo_file.write(new_item + '\n')  # Write the new item to the file with a newline character
    print("To-do item added successfully!")
except FileNotFoundError:
    print("The file 'todo.txt' was not found. Please make sure it exists.")


# ## Working With CSV Files:

# #### Writing a CSV:

# In[1]:


import csv

field_names = ['name', 'age']

data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28},
]

with open('team.csv', 'w+', newline='') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

    spreadsheet.writeheader()

    spreadsheet.writerows(data)


# #### Reading a CSV:

# In[5]:


import csv
with open('team.csv', 'r') as csv_file: 
    spreadsheet = csv.DictReader(csv_file) 
    for row in spreadsheet:
        print(dict(row))


# In[ ]:





# ### Exercise 5.2: This program is supposed to read data about trees from a file to find the shortest tree. Complete the program adding code to open trees.csv .

# 1. The trees.csv file is included with your student guides.
# 2. Save the csv file in the same folder as your Python program.

# In[6]:


# The file has been saved and uploaded in the same location.


# In[7]:


import csv

# Open the csv file and read its contents
with open('trees.csv', 'r') as csv_file:
    # Create a DictReader object to read the file as a dictionary
    spreadsheet = csv.DictReader(csv_file)
    
    heights = []  # List to store tree heights
    
    # Loop through each row in the CSV file
    for row in spreadsheet:
        # Extract the height of the tree from the 'height' column
        tree_height = float(row['height'])
        heights.append(tree_height)  # Add the height to the list

# Find the shortest tree height
shortest_height = min(heights)

# Print the shortest height
print(shortest_height)


# In[9]:


# This solution also gives same results
import csv

with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    heights = []

    for row in spreadsheet: 
        tree_height = row['height'] 
        heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)


# In[ ]:





# ## Python Pip:

# **pip:** A package manager used to install libraries that other people have written

# - pip is used via the terminal (command-line)

# #### Install the requests library using pip
# 
# - command-line
# - pip install requests

# ## APIs: Reading Stuff:

# **Application Programming Interface (API):** A way for different programs to interact. For example they
# can send data to one another.
# 
# 
# Web APIs allow you to interact with other programs over the internet.

# **API Request:** When your program asks an API for some or to complete a specific action
# 
#     
# **API Response:** The result of your request from the API

# Pokéapi is an API to get data about Pokémon
# 
# pokeapi.co/ (https://pokeapi.co/)

# - Each Pokemon has a number that identifies it
# - You can retrieve information about different Pokemon from urls
# 
# https://pokeapi.co/api/v2/pokemon/6/ (https://pokeapi.co/api/v2/pokemon/6/)

# In[ ]:


# Save this as get_pokemon.py


# In[2]:


import requests
from pprint import pprint

pokemon_number = input("What is the Pokemon's ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
print(response)

pokemon = response.json()
pprint(pokemon)


# In[10]:


import pandas as pd

# Create a dictionary with the data
data = {
    "Status Code": [200, 404, 400],
    "Name": ["OK", "Not Found", "Bad Request"],
    "Explanation": [
        "The request worked",
        "Couldn't find the URL you requested",
        "The request you made isn't understood"
    ]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
df


# ### Exercise 5.3: Get the height and weight of a specific Pokemon and print the output 
# 
# #### Extension: Print the names of all of a specific Pokemon's moves

# In[3]:


import requests

pokemon_number = input("What is the Pokemon's ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
pokemon = response.json()

print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])


# In[11]:


# Extension Solution
import requests

pokemon_number = input("What is the Pokemon's ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
pokemon = response.json()

moves = pokemon['moves']

for move in moves: 
    print(move['move']['name'])


# In[ ]:





# ## Recap:

# This session
# 1. Files
# 2. Pip package manager 3. APIs

# Question 1: What is a Web API?
# 
# **Web API** (Application Programming Interface) is a set of rules and protocols for building and interacting with software applications over the internet. It allows different software programs to communicate with each other. 
# 
# - **HTTP Requests**: Web APIs often use HTTP methods such as GET, POST, PUT, and DELETE to perform operations. 
# - **Endpoints**: They are accessed via specific URLs (endpoints) that represent different functionalities or data.
# - **Data Formats**: Web APIs usually exchange data in formats like JSON (JavaScript Object Notation) or XML (eXtensible Markup Language).
# 
# **Example**: A weather service API might allow you to request current weather conditions for a specific location by sending a request to a URL and receiving weather data in response.
# 
# ### Question 2: What is the Purpose of `pip` and PyPI?
# 
# - **`pip`**: 
#   - `pip` is the package installer for Python. It allows you to install, update, and remove Python packages from the command line. 
#   - Example command: `pip install requests` installs the `requests` package.
# 
# - **PyPI** (Python Package Index): 
#   - PyPI is the official repository of third-party Python packages. It hosts a wide range of libraries and tools developed by the Python community.
#   - When you use `pip` to install a package, `pip` retrieves it from PyPI.
# 
# ### Question 3: Explain What This Code Does
# 
# ```python
# import requests  # Import the requests library for making HTTP requests
# url = 'https://pokeapi.co/api/v2/item/28/'  # URL for the API endpoint
# response = requests.get(url)  # Send an HTTP GET request to the URL
# data = response.json()  # Parse the JSON response into a Python dictionary
# print(data['name'])  # Print the value associated with the 'name' key in the dictionary
# ```
# 
# **Explanation**:
# 
# 1. **`import requests`**:
#    - Imports the `requests` library, which is used for making HTTP requests.
# 
# 2. **`url = 'https://pokeapi.co/api/v2/item/28/'`**:
#    - Defines the URL of the API endpoint you are querying. This endpoint provides information about the Pokémon item with ID 28.
# 
# 3. **`response = requests.get(url)`**:
#    - Sends an HTTP GET request to the specified URL. The `requests.get()` function returns a response object that contains the server's response to the HTTP request.
# 
# 4. **`data = response.json()`**:
#    - Converts the response content from JSON format into a Python dictionary. The `.json()` method is used to parse the JSON data into a Python dictionary.
# 
# 5. **`print(data['name'])`**:
#    - Accesses and prints the value associated with the key `'name'` from the dictionary. This key represents the name of the Pokémon item with ID 28.
# 
# **In Summary**:
# This code retrieves information about a specific Pokémon item (with ID 28) from the PokeAPI and prints the item's name.

# In[12]:


import requests

url = 'https://pokeapi.co/api/v2/item/28/'

response = requests.get(url)
data = response.json()

print(data['name'])


# In[ ]:




