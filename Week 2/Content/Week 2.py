#!/usr/bin/env python
# coding: utf-8

# ## Week 2 - Problem Solving 

# In[ ]:





# This session:
# 1. User Input
# 2. Importing modules
# 3. For Loops
# 4. While Loops
# 5. Functions

# ## User Input:

# - The input( ) function allows you to input data after the program has started running.

# - This program uses input to ask what your name is:

# In[2]:


age = input('What is your age? ')
print('Hello, I am {} yo'.format(age))


# ### Exercise 2.1: Write a program that asks two questions using input() then prints the values that were entered. You can choose any questions that you want.

# In[4]:


fruit = input('What fruit do you like? ')
veg = input('What veg do you like? ')
print('You like {} and you like {}'.format(fruit, veg))


# - The int( ) function converts string value into integer values:

# In[5]:


apples_string = '12'
total_apples = int(apples_string) + 5

print(total_apples)


# - The input( ) always returns a string value. You can convert this string value to an integer with int():

# In[1]:


purchased_apples = input('How many apples did you buy? ')
print(type(purchased_apples))
total_apples = int(purchased_apples) + 5

print(total_apples)

type(0)


# ### Exercise 2.2: You have friends at your house for dinner and you've accidentally burnt the lasagne. Time to order pizza.

# - Write a program calculate how many pizzas you need to feed you and your friends.

# In[2]:


friends = input('How many friends? ')
pizzas = int(friends) * 0.5

print('You need {} pizzas for {} friends'.format(pizzas, friends))


# In[ ]:





# ## Python Modules:

# #### Module: Code that someone else has written that you can reuse in your programs.

# Modules are imported into your Python programs:
# `import `
# also
# `from import `

# #### Examples of python modules:
# 1. math --> mathematical functions
# 2. datetime --> date and time value manipulation
# 3. timeit --> time the execution of small blocks of Python code
# 4. re --> regular expressions (pattern search)
# 5. copy --> duplicating objects

# In[4]:


import datetime
x = datetime.datetime.now()

print(x)


# Datetime package has many useful functions:
# - We can find out date, time, timedate and even timedelta with this module
# - We can create dates by converting text into date objects
# - We can perform calculations to compute dates in the past and in the future

# In[ ]:





# ## Problem Solving (with datetime):

# Python datetime package documentation: https://docs.python.org/3/library/datetime.html (https://docs.python.org/3/library/datetime.html)
# 
#         
# After importing a module you can use the module's functions. For example, we can use the function that can tell us exactly what day and time it
# is now.

# In[ ]:





# ## Creating Date Objects:

# ### 1. Example Where This Code Would Be Useful
# 
# The code provided in your question could be useful in a context where you need to repeat a string multiple times based on a numeric value. While the code may not be the best example for realistic situations, consider a scenario where you might want to create a visual separator for a calendar layout. For example:
# 
# #### Example: Creating a Calendar Layout
# 
# Suppose you are generating a textual representation of a calendar. You could use a similar approach to create visual dividers or repeat characters to represent days.
# 
# ```python
# days = 7  # Suppose we are creating a weekly calendar
# divider = "-" * 20  # Creates a line of 20 dashes
# 
# # Creating a visual weekly separator
# week_separator = divider + "\n"  # A new line after the divider
# calendar_layout = (week_separator * days).strip()  # Repeat for each day and remove trailing new line
# 
# print(calendar_layout)
# ```
# 
# **Output:**
# ```
# --------------------
# --------------------
# --------------------
# --------------------
# --------------------
# --------------------
# --------------------
# ```
# 
# This code creates a repeated pattern that could help visually distinguish each day in a textual calendar.
# 
# ### 2. Have You Ever Heard About a Timestamp?
# 
# Yes, a **timestamp** is a numerical representation of a specific point in time. It is commonly used in computing to represent the date and time in seconds (or milliseconds) that have elapsed since a particular starting point (called the **epoch**), which is usually set at January 1, 1970, 00:00:00 UTC for Unix systems.
# 
# ### Example for "Creating Date Objects" with Timestamps
# 
# To work with timestamps and create date objects in Python, we typically use the `datetime` module. Below is an example that demonstrates how to work with timestamps and convert them into date objects:
# 
# ```python
# from datetime import datetime
# 
# # Example timestamp (Unix timestamp for September 1, 2023, 12:00 PM UTC)
# timestamp = 1693560000
# 
# # Convert timestamp to a datetime object
# date_object = datetime.fromtimestamp(timestamp)
# 
# print("Date Object:", date_object)  # Output will be: Date Object: 2023-09-01 12:00:00
# ```
# 
# #### Explanation:
# 
# 1. **Import the `datetime` module**: This module provides classes for manipulating dates and times in both simple and complex ways.
#    
# 2. **Timestamp Definition**: `timestamp` is set to `1693560000`, which is the number of seconds since the Unix epoch (January 1, 1970).
# 
# 3. **Convert to Date Object**: `datetime.fromtimestamp()` takes a timestamp and converts it into a `datetime` object, which represents the date and time corresponding to that timestamp.
# 
# #### Additional Example: Current Timestamp to Date Object
# 
# You can also use the current timestamp to get the present date and time:
# 
# ```python
# # Get current timestamp
# current_timestamp = datetime.now().timestamp()
# 
# # Convert current timestamp to a datetime object
# current_date_object = datetime.fromtimestamp(current_timestamp)
# 
# print("Current Date Object:", current_date_object)  # Example Output: Current Date Object: 2024-09-03 11:20:35.123456
# ```
# 
# This approach can be used in various applications, like logging events, recording time-based data, or scheduling tasks.

# In[5]:


days = 7  # Suppose we are creating a weekly calendar
divider = "-" * 20  # Creates a line of 20 dashes

# Creating a visual weekly separator
week_separator = divider + "\n"  # A new line after the divider
calendar_layout = (week_separator * days).strip()  # Repeat for each day and remove trailing new line

print(calendar_layout)


# In[6]:


from datetime import datetime

# Example timestamp (Unix timestamp for September 1, 2023, 12:00 PM UTC)
timestamp = 1693560000

# Convert timestamp to a datetime object
date_object = datetime.fromtimestamp(timestamp)

print("Date Object:", date_object)  # Output will be: Date Object: 2023-09-01 12:00:00


# In[7]:


# Get current timestamp
current_timestamp = datetime.now().timestamp()

# Convert current timestamp to a datetime object
current_date_object = datetime.fromtimestamp(current_timestamp)

print("Current Date Object:", current_date_object)  # Example Output: Current Date Object: 2024-09-03 11:20:35.123456


# In[ ]:





# ## Formatting date objects:

# In[8]:


import datetime

my_date = datetime.date(2020, 12, 31)

print(my_date.strftime("%d-%b-%Y"))


# In[ ]:





# ## Character codes examples:

# - %a: Returns the first three characters of the weekday, e.g. Wed.
# - %A: Returns the full name of the weekday, e.g. Wednesday.
# - %B: Returns the full name of the month, e.g. September.
# - %w: Returns the weekday as a number, from 0 to 6, with Sunday being 0.
# - %m: Returns the month as a number, from 01 to 12.
# - %p: Returns AM/PM for time.
# - %f: Returns microsecond from 000000 to 999999.
# - %Z: Returns the timezone.
# - %Y: Returns the year in four digit format
# - %b: Returns the first three characters of the month name.
# - %d: Returns day of the month, from 1 to 31.
# - %Y: Returns the year in four-digit format.
# - %H: Returns the hour.
# - %M: Returns the minute, from 00 to 59.
# - %S: Returns the second, from 00 to 59.

# In[ ]:





# ## For Loops:

# - for loop: allows you to repeat a block of code multiple times

# In[12]:


# think of range(5) as a collection of five digits in a box: 0,1,2,3,4 starting from a 0
# the FOR loop would iterate through every digit

for number in range(5):
    print(number)


# In[13]:


# think of any word as a collection of characters that we can iterte over
for character in 'Banana':
    print(character)


# In[14]:


# think of any word as a collection of characters that we can iterte over
for character in 'Banana':
    print(character)
# print('<' + character + '>') # this action will be repeated for each character in the word!


# In[15]:


# think of this examples as a box with words, we are doing an action for each word
#NB: this is called a 'list' but we will learn about it later in the course, this is only an example for now.

for name in ['Mary', 'Ranjit', 'Fatima']:
    print(name)


# FOR LOOP:
# 
# - A for loop is used to iterate over sequences (a collection of items).
# - And not only just the sequences but any iterable object can also be traversed.
# - The execution will start and look for the first item in the sequence.
# - After executing the statements in the block, it will look for the next item and the process will continue until the the last item is reached.

# In[16]:


for number in range(5): # 0,1,2,3,4
    print("executing FOR LOOP - run No {}".format(number + 1))


# In[17]:


total = 0
print("*** This statement is OUTSIDE THE LOOP")
print("Before the loop executes, our TOTAL is equal to = ", total,
'\n')
print("--------------------------------------------------------")

for number in range(3): # remember --> 0, 1, 2
    
    print("This is loop execution for digit: " + str(number) + " inside the loop \n")
    print("Updating total... (+ 1) \n")

    total = total + 1 # every time the loop executes, we add 1 to the total

    
print("--------------------------------------------------------")
print("***This statementWe is OUTSIDE the loop now")
print("The final TOTAL value is: " + str(total))


# In[ ]:





# ## While Loop:

# - A while loop in python is used to iterate over a block of code or statements as long as the test expression is true.

# WHILE loop
# 
# - In case of a while loop a user does not know beforehand how many iterations are going to take place.
# - Beware of infinite while loops - they execute infinite times i we don't specify correct condition
# - If the loop is running infinitely and never stops, we would 'blow' our memory usage and the program would encounter an error.

# ### Example: Due to social disctancing, only 10 people are allowed to be inside a shot at the same time. This program invites people in the queue to come in while we have some capacity.

# In[18]:


store_capacity = 5 #

while store_capacity > 0:
    print('Please come in. Spaces available: ' + str(store_capacity))
    store_capacity = store_capacity - 1

print("\nPlease wait for someone to exit the store.")


# In[ ]:


# Example INFINITE 'while loop' that runs forever until the memory is 'blown'

store_capacity = 10

while store_capacity > 0:
    print('Please come in. Spaces available: ' + str(store_capacity))
    # store_capacity = store_capacity - 1 ---> imagine that we forgot to add this logic!!!


print("\nPlease wait for someone to exit the store.")


# 1. While loop is also very useful for the programming algorithms and program flow control.
# 2. We will practice more examples of while loop when we learn about IF/ELSE logic (as they go hand in hand)

# ## Functions:

# #### Function: is a reusable block of code that contains one or more Python statements and used for performing a specific task.

# ### Why use function in Python?
# 1. **Code re-usability:** it is better to wrap 10 lines of code in a function and just call the function wherever needed, as opposed to writing those 10 identical lines every time you perform that task.
# 2. **Improves Readability:** By using functions for frequent tasks you make your code structured and readable.
# 3. **Avoid redundancy:** When you no longer repeat the same lines of code throughout the code and use functions in places of those, you actually avoiding the redundancy that you may have created by not using functions.

# ## Create a Function

# - To define a Python function, use def keyword.
# - Here’s the simplest possible function that prints a greeting

# In[3]:


def hello():
print ('Hello, class!')


# In[9]:


def hello():
    print('Hello, class!')

hello()


# ## Call a Function
# - The def statement only creates a function but does not call it.
# - After the def has run, you can can call (in other words run) the function by adding parentheses after its name.

# In[6]:


def hello():
print('Hello, class ***!')
hello()


# In[7]:


def hello():
    print('Hello, class ***!')

hello()


# ## Pass Arguments
# - You can send information to a function by passing values, known as arguments.
# - Arguments are declared after the function name in parentheses.
# - When you call a function with arguments, the values of those arguments are copied to their corresponding parameters inside the function.

# In[14]:


# Pass single argument to a function
def hello(name):
    print('Hello,', name)

hello('Maria')
hello('Kim')
hello('Olya')


# In[15]:


# Pass multiple arguments
def some_function(name, job):
    print(name, 'is a', job)
    
some_function('developer', 'Fiona')


# # Function Arguments

# #### Types of arguments
# Python supports multiple types of arguments in the function definition:
# - Positional Arguments
# - Keyword Arguments
# - Default Arguments
# - Variable Length Positional Arguments (*args)
# - Variable Length Keyword Arguments (**kwargs)

# #### Positional Arguments
# - Positional arguments values are copied to their corresponding parameters in order.
# - You must to pass arguments in the order in which they are defined.

# In[16]:


# Correct arguments order
def some_function(name, job):
    print(name, 'is a', job)
    
some_function('Fiona', 'developer')


# In[18]:


# Wrong arguments order
def some_function(name, job):
    print(name, 'is a', job)

some_function('developer', 'Fiona')


# ## Keyword Arguments
# - you can pass arguments using the names of their corresponding parameters.
# - in this case, the order of the arguments no longer matters.
# - you can combine positional and keyword arguments in a single call.
# - if you do so, specify the positional arguments before keyword arguments.

# In[19]:


def some_function(name, job):
    print(name, 'is a', job)
    
some_function(job='developer', name='Fiona')

some_function(name='Fiona', job='developer')


# ## Default Arguments
# - You can specify default values for arguments when defining a function.
# - The default value is used IF the function is called without a corresponding argument.

# In[20]:


def some_function(name, job='developer'):
    print(name, 'is a', job)
    
some_function('Fiona')

some_function('Fiona', 'manager')


# # Returning Values from Function

# ### Return Value
# - To return a value from a function, simply use a return statement.
# - Once a return statement is executed, nothing else in the function body is executed.
# - Remember! a python function ALWAYS returns a value.
# - So, if you do not include any return statement, it automatically returns None.

# In[21]:


# Using return statement

def sum(x, y):
    return x + y


result = sum(10, 15)

print("result is: {}".format(result))


# In[27]:


# Without return statement

def sum(x, y):
    print(x + y)

    
result = sum(10, 15)
print("result is: {}".format(result))


# In[23]:


# Without return statement
def sum(x, y):
    x + y
    
result = sum(10, 15)
print("result is: {}".format(result))


# #### **Exercise 2.6:** Complete the function to return the area of a circle

# Use the comments to help you

# In[ ]:


def circle_area(): # add the radius argument inside the brackets
    area = 3.14 * (radius ** 2)
    # add return statement
    
circle_1 = circle_area(10)

print(circle_1)


# In[28]:


def circle_area(radius):  # add the radius argument inside the brackets
    area = 3.14 * (radius ** 2)
    return area
    # add return statement

circle_1 = circle_area(10)

print(circle_1)


# 1. **Define the Function:**
#    ```python
#    def circle_area(radius):
#    ```
#    This line defines a function named `circle_area` that takes one input, `radius`. The input `radius` is the distance from the center of the circle to its edge.
# 
# 2. **Calculate the Area:**
#    ```python
#    area = 3.14 * (radius ** 2)
#    ```
#    Inside the function, this line calculates the area of the circle using the formula \( \text{area} = \pi \times \text{radius}^2 \). We use `3.14` as an approximation for \(\pi\). The `**` operator is used to square the radius.
# 
# 3. **Return the Area:**
#    ```python
#    return area
#    ```
#    This line tells the function to give back (`return`) the calculated area to wherever the function was called.
# 
# 4. **Call the Function:**
#    ```python
#    circle_1 = circle_area(10)
#    ```
#    Here, we call the `circle_area` function with `10` as the radius. The function calculates the area for a circle with a radius of 10 and returns the result. We store this result in the variable `circle_1`.
# 
# 5. **Print the Result:**
#    ```python
#    print(circle_1)
#    ```
#    Finally, we print the value stored in `circle_1`, which is the area of the circle with a radius of 10.

# This code defines a function called `circle_area` that calculates the area of a circle based on a given radius. The function takes one argument, `radius`, and uses the formula \( π×radius 2) to calculate the area, with \(π) approximated as 3.14. The calculated area is then returned by the function. The function is called with a radius of 10, and the resulting area is stored in the variable `circle_1`. Finally, the value of `circle_1` is printed, showing the area of the circle with a radius of 10, which is 314.0.

# In[30]:


def circle_area(radius):
    area = 3.14 * (radius ** 2)
    return round(area, 2)  # To return it to a specific decimal place

circle_1 = circle_area(10)

print(circle_1)


# In[31]:


def circle_area(radius):
    area = 3.14 * (radius ** 2)
    return round(area, 2)

circle_1 = circle_area(10)

print(f"{circle_1:.2f}") # This is for different formatting


# In[25]:


def circle_area(radius):
    area = 3.14 * (radius ** 2)
    return area

area = circle_area(9)
print(area)


# ## What's the outcome of this?

# In[24]:


def days_in_hours(days):
    hours = days * 24
    return hours

print(days_in_hours(10))


# ## Combine FOR loop and FUNCTION

# In[32]:


def times_two(num):
    result = num * 2
    return result

for number in range(3): # 0,1,2
    calc_res = times_two(number)
    print(calc_res)


# In[ ]:




