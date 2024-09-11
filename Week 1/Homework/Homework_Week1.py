#!/usr/bin/env python
# coding: utf-8

# # Homework, Session 1

# ### Question 1:
# 
# **I am building some very high quality chairs and need exactly four nails for each chair. I've written a program to calculate how many nails I need to buy to build these chairs.**

# In[1]:


chairs = '15' 
nails = 4 

total_nails = chairs * nails 

message = 'I need to buy {} nails'.format(total_nails) 

print('You need to buy {} nails'.format(message))


# 1. When I run the program it tells me that I need to buy 15151515 nails. This seems like a lot of nails. 
# 2. Is my program calculating the total number of nails correctly? What is the problem? How do I fix it? 

# In[ ]:





# The issue is in the program that the variable `chairs` is a string ('15') rather than an integer. When you multiply a string by an integer, Python repeats the string instead of performing numerical multiplication. That's why you're seeing `15151515` nails, which is just the string '15' repeated 4 times.
# 
# Here's how to fix the problem:
# 
# 1. Convert the `chairs` variable from a string to an integer.
# 2. Then perform the multiplication to get the correct number of nails.
# 
# Here's the corrected version of the program:
# 
# ```python
# chairs = 15  # Change '15' to the integer 15
# nails = 4
# total_nails = chairs * nails
# message = 'I need to buy {} nails'.format(total_nails)
# print(message)  # Print the message directly, since it's already formatted
# ```
# 
# In this version:
# - `chairs` is assigned the integer value `15`.
# - The calculation `total_nails = chairs * nails` performs the correct numerical multiplication.
# - The `message` string is formatted correctly with the total number of nails.
# - Finally, `print(message)` outputs the correct message.
# 
# This will correctly calculate and display the number of nails needed.

# In[2]:


chairs = 15  # Change '15' to the integer 15
nails = 4
total_nails = chairs * nails

message = 'I need to buy {} nails'.format(total_nails)
print(message)  # Print the message directly, since it's already formatted


# In[ ]:





# ### Question 2:
# 
# **I'm trying to run this program, but I get an error. What is the error telling me is wrong? How do I fix the program?**

# In[3]:


my_name = Penelope 
my_age = 29 

message = 'My name is {} and I am {} years old'.format(my_name, my_age) 
print(message) 


# In[4]:


my_name = 'Penelope' 
my_age = 29 

message = 'My name is {} and I am {} years old'.format(my_name, my_age) 
print(message) 


# In[ ]:





# ### Question 3:
# 
# **I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make. Write a program to calculate this.**

# Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be able to easily change these values if I want. The output should say something like "You can make 9 omelettes with 6 boxes of eggs". 

# In[5]:


# Define variables
eggs_per_box = 6
eggs_per_omelette = 4
number_of_boxes = 6

# Calculate total number of eggs
total_eggs = eggs_per_box * number_of_boxes

# Calculate the number of omelettes that can be made
omelettes = total_eggs // eggs_per_omelette  # Use integer division to get the whole number of omelettes

# Format and print the message
message = 'You can make {} omelettes with {} boxes of eggs'.format(omelettes, number_of_boxes)
print(message)


# In[ ]:




