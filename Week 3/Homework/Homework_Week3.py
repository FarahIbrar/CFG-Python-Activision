#!/usr/bin/env python
# coding: utf-8

# # Homework, Session 3

# ### Question 1:
# 
# **Create a program that tells you whether or not you need an umbrella when you leave the house.**
# 
# The program should: 
# 1. Ask you if it is raining using input() 
# 2. If the input is 'y', it should output 'Take an umbrella' 
# 3. If the input is 'n', it should output 'You don't need an umbrella' 

# In[1]:


# Ask if it is raining
is_raining = input("Is it raining? (y/n): ")

# Check the user's input and provide the appropriate response
if is_raining == 'y':
    print("Take an umbrella")
elif is_raining == 'n':
    print("You don't need an umbrella")
else:
    print("Please enter 'y' for yes or 'n' for no")


# In[ ]:





# ### Question 2:
# 
# **I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit. I've written a program to check that I can afford the cost, but something doesn't seem right.** 
# 
# - **Have a look at my program and work out what I've done wrong**

# In[2]:


my_money = input('How much money do you have? ') 
boat cost = 20 + 5

if my_money < boat_cost: 
    print('You can afford the boat hire') 
else: 
    print('You cannot afford the board hire') 


# There are a few issues with the program that need fixing:
# 
# 1. **Input Handling**: The `input()` function returns a string, so you need to convert it to a number (e.g., float or int) before comparison.
# 2. **Variable Name**: The variable `boat cost` has a space in it, which is not allowed in variable names. It should be `boat_cost`.
# 3. **Comparison Logic**: The `if` condition should check if `my_money` is greater than or equal to `boat_cost`.
# 
# Here’s the corrected version of the program:
# 
# ```python
# # Ask how much money the user has
# my_money = float(input('How much money do you have? '))
# 
# # Define the cost of hiring the boat
# boat_cost = 20 + 5
# 
# # Check if the user has enough money
# if my_money >= boat_cost:
#     print('You can afford the boat hire')
# else:
#     print('You cannot afford the boat hire')
# ```
# 
# ### Explanation:
# 1. `float(input(...))` converts the user’s input into a floating-point number so it can be compared with `boat_cost`.
# 2. The variable `boat_cost` is used without spaces.
# 3. The `if` condition now correctly checks if `my_money` is greater than or equal to `boat_cost` to determine if the user can afford the boat hire.

# In[3]:


# Ask how much money the user has
my_money = float(input('How much money do you have? '))

# Define the cost of hiring the boat
boat_cost = 20 + 5

# Check if the user has enough money
if my_money >= boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the boat hire')


# ### What's Fixed:
# 1. Converted `my_money` from a string to a float so you can do numerical comparisons.
# 2. Changed `boat cost` to `boat_cost` to fix the variable name issue.
# 3. Adjusted the `if` condition to check if `my_money` is greater than or equal to `boat_cost`.

# In[ ]:





# ### Question 3:
# 
# **Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to quickly categorise books by the century and decade that they were written.**
# 
# **Write a program that takes a year (e.g. 1872) and outputs the century and decade (e.g. "Nineteenth Century, Seventies").**

# In[5]:


# Get the year from the user
year = int(input("Enter the year the book was written (between 1800 and 1950): "))

# Calculate the century
if 1800 <= year < 1900:
    century = "Nineteenth Century"
elif 1900 <= year <= 1950:
    century = "Twentieth Century"

# Calculate the decade
decade = (year // 10) % 10 * 10
decade_names = {
    180: "Eighteen",
    190: "Nineteen",
}

decade_str = decade_names.get(year // 100 * 100, "Unknown") + f"{decade}"

# Output the result
print(f"{century}, {decade_str}")


# In[ ]:




