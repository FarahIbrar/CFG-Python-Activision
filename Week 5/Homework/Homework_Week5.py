#!/usr/bin/env python
# coding: utf-8

# # Homework, Session 5

# ### Question 1:
# 
# **You're having coffee/tea/beverage of your choice with a friend that is learning to program in Python. They're curious about why they would use pip. Explain what pip is and one benefit of using pip.**

# `pip` is a tool used in Python to install and manage libraries and packages that are not included in Python by default. 
# 
# **One benefit of using `pip`** is that it allows you to easily add new features to your Python programs without having to write all the code yourself. You can quickly install packages like `numpy` for math, `requests` for web requests, and many others with just one command.

# In[ ]:





# ### Question 2:
# 
# **This program should save my data to a file, but it doesn't work when I run it. What is the problem and how do I fix it?**

# In[1]:


poem = 'I like Python and I am not very good at poems' 

with open('poem.txt', 'r') as poem_file: 
    poem_file.write(poem) 


# In[3]:


poem = 'I like Python and I am not very good at poems'

# Write to the file
with open('poem.txt', 'w') as poem_file: 
    poem_file.write(poem)

# Read from the file
with open('poem.txt', 'r') as poem_file:
    output = poem_file.read()
    print(output)


# In[ ]:





# ### Question 3:
# 
# **In this session you used the Pokemon API to retrieve a single Pokemon. I want a program that can retrieve multiple Pokemon and save their names and moves to a file.**
# 
# **Use a list to store about 6 Pokemon IDs. Then in a for loop call the API to retrieve the data for each Pokemon. Save their names and moves into a file called 'pokemon.txt'**

# In[5]:


import requests

# List of Pokémon IDs
pokemon_ids = [1, 4, 7, 10, 13, 16]

# Open the file in write mode
with open('pokemon.txt', 'w') as file:
    # Loop through each Pokémon ID
    for poke_id in pokemon_ids:
        # Call the API to get data for the Pokémon
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_id}')
        data = response.json()

        # Get the Pokémon's name and moves
        name = data['name']
        moves = [move['move']['name'] for move in data['moves']]
        
        # Write the name and moves to the file
        file.write(f'Name: {name}\n')
        file.write('Moves:\n')
        for move in moves:
            file.write(f'- {move}\n')
        file.write('\n')

# Read the file and print its contents
with open('pokemon.txt', 'r') as file:
    content = file.read()
    print(content)


# In[ ]:




