#!/usr/bin/env python
# coding: utf-8

# In[3]:


"Cat"


# In[4]:


"Cat" + " videos"


# In[5]:


"Cat" * 3


# In[9]:


"Cat" + 3 + "Cat".upper()


# In[7]:


"Cat".lower()


# In[8]:


"the lord of the rings".title()


# ### What is the output for each one and why?

# One of them causes an exception. Read the exception message. 
# 
# ```Python
# "Cat" + 3 + "Cat".upper()
# ```
# 
# ```Python
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Cell In[9], line 1
# ----> 1 "Cat" + 3 + "Cat".upper()
# 
# TypeError: can only concatenate str (not "int") to str
# ```
# 
# - This line is causing the syntax error because it's not valid Python syntax. You can't concatenate a string and an integer directly, and there's also no valid syntax for "Cat" + 3 "Cat".upper().
# 
# - To fix it, you need to either:
# 
# - Convert the integer to a string using str()
# - Format it properly if you're trying to concatenate and manipulate strings.
# 
# ```Python 
# For example:
# "Cat" + str(3) + "Cat".upper()
# This will result in: "Cat3CAT".
# ```

# In[10]:


"Cat" + str(3) + "Cat".upper()


# In[ ]:





# ## Method:

# ### "method:" A repeatable piece of code that completes a task for specic data-type
# 
# - Methods are like funcitons, but they are tied to a specic data-types e.g. .upper() can only used with a string and not an integer.

# In[11]:


print("Cat" + 3)


# - Will cause this exception (above)

# The error occurred because you tried to concatenate a string (`"Cat"`) with an integer (`3`). In Python, the `+` operator is used to concatenate strings, but both operands must be strings. When Python sees that one of the operands is an integer, it raises a `TypeError`.
# 
# #### Explanation of the Error
# 
# - **Error Message:** `TypeError: can only concatenate str (not "int") to str`
#   - This means that Python cannot concatenate a string with a non-string type (in this case, an integer).
# 
# #### How to Fix the Error
# 
# To fix this, you need to convert the integer to a string using the `str()` function. This way, both operands are strings, and Python can concatenate them.
# 
# #### Corrected Code
# 
# ```python
# print("Cat" + str(3))
# ```
# 
# #### Why This Fix Works
# 
# - **Conversion to String:** `str(3)` converts the integer `3` to the string `"3"`.
# - **Concatenation:** Now, the expression `"Cat" + "3"` is a valid string concatenation.
# 
# **Output:**
# ```
# Cat3
# ```
# 
# This works because both `"Cat"` and `"3"` are now strings, and Python can concatenate them without any issues.

# In[12]:


print("Cat" + str(3))


# In[ ]:





# ## Variables:

# ### "Variable:"" a reusable label for a data value in Python.
# 
# 
# Creating (assigning) a variable has three parts:

# 1. The variable's name
# 2. An equals sign =
# 3. The data value it references

# ```python 
# username = 'sarah_1987' 
# age = 23
# ```
# 
# - Values and variables are interchangeable
# - A variable can be put anywhere that a data value can be used

# In[13]:


print('spaghetti')


# In[15]:


food = 'spaghetti'
print(food)

# Variables can be reused.


# In[18]:


# This program calculates the cost of 12 oranges.

oranges = 12
cost_per_orange = 0.5
total_cost = oranges * cost_per_orange
print(str(oranges) + " oranges") 
print("costs " + str(total_cost))

# The oranges variable is reused twice in the program


# ### Exercise 1.4: In a new Python **le** called cat_food.py, create a program that calculates how many cans of cat food you need to feed 10 cats Your will need:
# 
# 1. A variable for the number of cats
# 2. A variable for the number of cans each cat eats in a day 3. A print() function to output the result
# 
# - Extension: change the calculation to work out the amount needed for 7 days.

# In[25]:


# cat_food.py

# 1. Variable for the number of cats
number_of_cats = 10

# 2. Variable for the number of cans each cat eats in a day
cans_per_cat_per_day = 2

# 3. Calculate the total number of cans needed for 1 day
total_cans_for_1_day = number_of_cats * cans_per_cat_per_day

# 4. Extension: Calculate the total number of cans needed for 7 days
total_cans_for_7_days = total_cans_for_1_day * 7

# 5. Print the results using string concatenation with +
print("Total cans needed for 1 day: " + str(total_cans_for_1_day))
print("Total cans needed for 7 days: " + str(total_cans_for_7_days))


# In[ ]:





# ## String Formatting:

# Python strings have a method ( .format() ) that substitutes place-holders {} for values.

# In[21]:


oranges = 12
cost_per_orange = 0.5
total_cost = oranges * cost_per_orange
output = "{} oranges costs £{}".format(oranges, total_cost)
print(output)


# This could have been written as:

# In[24]:


oranges = 12 
cost_per_orange = 0.5
total_cost = oranges * cost_per_orange
output = str(oranges) + " oranges costs £" + str(total_cost) 
print(output)


# ### Exercise 1.5: Rewrite cat_food.py to use string formatting instead of joining strings with + .

# In[26]:


# cat_food.py

# 1. Variable for the number of cats
number_of_cats = 10

# 2. Variable for the number of cans each cat eats in a day
cans_per_cat_per_day = 2

# 3. Calculate the total number of cans needed for 1 day
total_cans_for_1_day = number_of_cats * cans_per_cat_per_day

# 4. Extension: Calculate the total number of cans needed for 7 days
total_cans_for_7_days = total_cans_for_1_day * 7

# 5. Print the results using string formatting (f-strings)
print(f"Total cans needed for 1 day: {total_cans_for_1_day}")
print(f"Total cans needed for 7 days: {total_cans_for_7_days}")


# In[ ]:





# ## Comments:

# ### Comment: a way for a programmer to write human-readable notes in their code. When running a program, comments are ignored by Python.

# In[27]:


# This is a comment
# Comments in Python start with a '#'


# In[28]:


# A program to calculate the cost of some oranges
oranges = 12 
cost_per_orange = 0.5

total_cost = oranges * cost_per_orange
output = "{} oranges costs £{}".format(oranges, total_cost) 
print(output)


# In[ ]:





# ## Recap:

# 1. Run Python with les and console 
# 2. Data types (Integers, Floats and Strings) 
# 3. Maths operations
# 4. Understanding Error Messages
# 5. Variables

# ### Question 1: What are the names of the math operators?
# 
# In Python, the primary math operators are:
# 
# 1. **Addition (`+`)**: Adds two numbers. Example: `3 + 2 = 5`
# 2. **Subtraction (`-`)**: Subtracts the second number from the first. Example: `5 - 3 = 2`
# 3. **Multiplication (`*`)**: Multiplies two numbers. Example: `4 * 3 = 12`
# 4. **Division (`/`)**: Divides the first number by the second, returning a float. Example: `10 / 2 = 5.0`
# 5. **Floor Division (`//`)**: Divides the first number by the second, returning an integer result. Example: `10 // 3 = 3`
# 6. **Modulus (`%`)**: Returns the remainder of the division. Example: `10 % 3 = 1`
# 7. **Exponentiation (`**`)**: Raises the first number to the power of the second. Example: `2 ** 3 = 8`
# 
# ### Question 2: When should you use a Python file and when should you use the Python console?
# 
# - **Python File (.py)**:
#   - Use it when you want to write, save, and run scripts or programs.
#   - Suitable for developing larger projects, scripts that need to be reused, or programs that require a well-organized structure.
#   - Files can be edited, shared, and maintained.
#   - Helpful for running a series of statements that work together.
# 
# - **Python Console (Interpreter/REPL - Read-Eval-Print Loop)**:
#   - Use it for quick calculations, testing small code snippets, or debugging.
#   - Useful for immediate feedback and interactive experimentation.
#   - Great for beginners to learn Python and test small chunks of code.
#   - Not suitable for running large, complex, or long-term scripts, as code is not saved after the session ends.
# 
# ### Question 3: What is the output of this code?
# 
# ```python
# days = 31
# hours = "24"
# total_hours = days * hours
# msg = "There are {} in {} days".format(total_hours, days) 
# print(msg)
# ```
# 
# **Explanation**:
# 
# 1. `days` is an integer with a value of `31`.
# 2. `hours` is a string with a value of `"24"`.
# 3. `total_hours = days * hours` multiplies the integer `days` with the string `hours`. In Python, multiplying an integer by a string results in the string being repeated that many times. So, `total_hours` will be `"242424... (31 times)"`.
# 4. The `msg` string is formatted with `total_hours` and `days`.
# 
# **Output**:
# ```
# There are 242424242424242424242424242424 in 31 days
# ```
# 
# The string `"24"` is repeated 31 times as a result of the multiplication.
