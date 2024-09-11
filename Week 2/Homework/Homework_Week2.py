#!/usr/bin/env python
# coding: utf-8

# # Homework, Session 2

# ### Question 1:
# 
# **Explain what this program does (below).**

# In[3]:


for number in range(100): 

    output = 'o' * number 
    print(output) 


# This program prints a series of lines with increasing numbers of 'o' characters.
# 
# Here's a step-by-step explanation:
# 
# 1. `for number in range(100):` - This creates a loop that iterates 100 times, with `number` taking values from 0 to 99.
# 
# 2. `output = 'o' * number` - This line creates a string consisting of 'o' characters repeated `number` times.
# 
# 3. `print(output)` - This prints the string `output` to the screen.
# 
# So, for each iteration, the program prints a line with `number` 'o' characters. The first line has 0 'o's, the second line has 1 'o', the third line has 2 'o's, and so on up to 99 'o's on the last line.

# In[ ]:





# ### Question 2:
# 
# **Your boss really likes calculating VAT on their purchases. It is their favourite hobby. They've written this code to calculate VAT and need your help to fix it.**

# In[4]:


def calculate_vat(amount): 
    amount * 1.2 

total = calculate_vat(100)
print(total) 


# #### When your boss runs the program they get the following output: 
# None 
# 
# Your boss expects the program to output the value 120. 
# 1. What is wrong? 
# 2. How do you fix it? 

# In[5]:


def calculate_vat(amount):
    return amount * 1.2  # Add return to provide the result of the calculation

total = calculate_vat(100)
print(total)  # This will now print 120


# The issue with the program is that the `calculate_vat` function does not return any value. By default, if a function does not explicitly return a value, it returns `None`.
# 
# #### Explanation:
# 1. `return amount * 1.2` ensures that the result of the VAT calculation is returned by the function.
# 2. When `calculate_vat(100)` is called, it now correctly returns `120`, which is assigned to `total` and then printed.

# In[ ]:




