#!/usr/bin/env python
# coding: utf-8

# ## Week 3 - Decision making logic

# #### Starter: Rewrite this code to use a for loop and the range() function:

# In[1]:


print('~' * 0)
print('~' * 1)
print('~' * 2)
print('~' * 3)
print('~' * 4)
print('~' * 5)
print('~' * 6)
print('~' * 7)
print('~' * 8)


# In[1]:


for i in range(9):
    print('~' * i)


# ## Topics in this session:
# 
# 1. Comparison Operators
# 2. Logical Operators
# 3. If Statements

# ## Comparisons and Logical Operators:

# **Bolean:** A data-type that is either `True` or `False`
# 
# **Comparison operator:** compare values to determine wheter something is `True` or `False`

# In[ ]:





# This code checks if the user has input '`Monday`' using the == operator

# In[3]:


today = input('What day is it? ')

is_thursday = today == 'Thursday'

print('Today is Thursday: {}'.format(is_thursday))


# ## Summary of comparison operators in Python:

# | Operator                | Description                        |
# |-------------------------|------------------------------------|
# | `==`                    | Equal to                            |
# | `!=`                    | Not equal to                        |
# | `>`                     | Greater than                        |
# | `<`                     | Less than                           |
# | `>=`                    | Greater than or equal to            |
# | `<=`                    | Less than or equal to               |
# 

# `float()` can convert strings to oats
# 
# This code checks if the current temperature is freezing:

# In[6]:


temperature = input('What is the temperature? ')
is_freezing = float(temperature) <= 0.0
print('The temperature is freezing: {}'.format(is_freezing))


# ### **Exercise 3.1:**  You have a budget of £10 and want to write a program to decide which burger restaurant to go to.
# 
# 1. Input the price of a burger using input()
# 2. Check whether the price is less than or equal (<=) 10.00
# 3. Print the result in the format below
# `Burger is within budget: True`
# 
# **Hint:** remember to convert the input from a string to a decimal with `float()`

# In[1]:


price = input('How much is a burger?')

is_within_budget = float(price) <= 10.00

print('Burger is within budget: {}'.format(is_within_budget))


# ### There are logical operators to combine multiple checks

# | Operator    | Description                               | Example                                      |
# |-------------|-------------------------------------------|----------------------------------------------|
# | `and`       | Returns `True` if both expressions are `True` | `True and True` evaluates to `True`           |
# | `or`        | Returns `True` if at least one expression is `True` | `True or False` evaluates to `True`           |
# | `not`       | Reverses the expression                   | `not True` evaluates to `False`, `not False` evaluates to `True` |

# #### This program will work out if you should visit Mars based on whether you want to visit and if you can afford it:

# In[3]:


mars_choice = input('Would you like to visit Mars? y/n ')
is_willing = mars_choice == 'y'

affordable = input('Can you afford to visit Mars? y/n ')
can_afford = affordable == 'y'

should_visit_mars = is_willing and can_afford

print('You should visit Mars: {}'.format(should_visit_mars))


# ### Exercise 3.2: Add code to your burger program to input whether the restaurant has a vegetarian option 
# 
# The output should say whether the cost is within budget **AND** has a vegetarian option
# 
# `Restaurant meets criteria: True`

# In[10]:


price = float(input('How much is a burger?'))
is_within_budget = price <= 10.00
vegetarian_option = input('Does the restaurant offer a vegetarian option? (y/n) ')
meets_criteria = is_within_budget and vegetarian_option
print('Restaurant meets criteria:', meets_criteria)


# In[12]:


price = float(input('How much is a burger? '))
is_within_budget = price <= 10.00
vegetarian_option = input('Does the restaurant offer a vegetarian option? (y/n) ')

# Check if vegetarian_option is exactly 'y'
has_vegetarian_option = vegetarian_option == 'y'

meets_criteria = is_within_budget and has_vegetarian_option
print('Restaurant meets criteria:', meets_criteria)


# In[ ]:





# In[13]:


vegetarian_choice = input('Does your restaurant has a vegetarian option? y/n ')
is_answering = vegetarian_choice == 'y'
price= input('How much is a burger? ')
within_budget = float(price) <= 10
is_good_choice= vegetarian_choice and within_budget
print('Restaurant meets criteria: {}'.format(is_good_choice))


# In[ ]:


vegetarian_choice = input('Does your restaurant have a vegetarian option? y/n ')
is_answering = vegetarian_choice == 'y'

price = input('How much is a burger? ')
within_budget = float(price) <= 10

is_good_choice = is_answering and within_budget  # Check if both conditions are True
print('Restaurant meets criteria: {}'.format(is_good_choice))


# In[ ]:





# ## If Statements:

# **if statement:** used to run a block of code depending on whether a condition is `True` or `False`

# In[15]:


password = input('password: ')
if password == 'jumanji':
    print('Success!')


# In[ ]:


An if statement has the following:

1. The if keyword
2. A condition (comparison)
3. A colon
4. Body (indented four spaces)


# In[ ]:





# #### This program checks whether you are an admin and you have entered the right password:

# In[16]:


name = input("What is your name? ")
is_admin = name == 'admin'
password = input("What is your password? ")
is_password_correct = password == 'dinosaurs'
if is_admin and is_password_correct:
    print('Welcome')
if not is_admin or not is_password_correct:
    print('Go away')


# In[ ]:





# ### **Exercise 3.3:** Rewrite the output of your burger program to use if statements

# If it is a good choice it should be:
# `This restaurant is a great choice!`
# 
# If it is not a good choice it should be:
# `Probably not a good idea`

# #### Reminder of the code:
# 
# ```python
# vegetarian_choice = input('Does your restaurant has a vegetarian option? y/n ')
# is_answering = vegetarian_choice == 'y'
# price= input('How much is a burger? ')
# within_budget = float(price) <= 10
# is_good_choice= vegetarian_choice and within_budget
# print('Restaurant meets criteria: {}'.format(is_good_choice))
# ```

# In[17]:


vegetarian_choice = input('Does your restaurant have a vegetarian option? y/n ')
is_answering = vegetarian_choice == 'y'
price = input('How much is a burger? ')
within_budget = float(price) <= 10
is_good_choice = is_answering and within_budget

if is_good_choice:
    print('This restaurant is a great choice!')
else:
    print('Probably not a good idea')


# In[ ]:





# ## Else Statements:

# **else statement:** Used with an `if` statement and will run when the `if` condition is `False`

# In[18]:


password = input('password: ')
if password == 'jumanji':
    print('Success!')
else:
    print('Failure!')


# #### Here's the admin program rewritten to use else :

# In[19]:


name = input("What is your name? ")
is_admin = name == 'admin'
password = input("What is your password? ")
is_password_correct = password == 'dinosaurs'
if is_admin and is_password_correct:
    print('Welcome')
else:
    print('Go away')


# In[ ]:





# ### Exercise 3.4: Now that you've nished your burger, you want to pay for your food. Let's write a program to calculate your meal and apply a discount if applicable.

# If your total meal costs more than £20 and you have a discount, the price will be reduced by 10%.
# The program should print "Discount applied" or "No discount" depending on whether the discount
# criteria was met.

# In[ ]:


vegetarian_choice = input('Does your restaurant have a vegetarian option? y/n ')
is_answering = vegetarian_choice == 'y'
price = input('How much is a burger? ')
within_budget = float(price) <= 10
is_good_choice = is_answering and within_budget

if is_good_choice:
    print('This restaurant is a great choice!')
else:
    print('Probably not a good idea')

meal_cost = float(input('What is the total cost of your burger meal: '))
has_discount = input('Do you have a discount? y/n ') == 'y'

if meal_cost > 20 and has_discount:
    meal_cost *= 0.90 
    print('Discount applied')
else:
    print('No discount')

print('Total cost to pay: £{}'.format(format(meal_cost, '.2f')))


# In[2]:


# Existing code for checking restaurant choice
vegetarian_choice = input('Does your restaurant have a vegetarian option? y/n ')
is_answering = vegetarian_choice == 'y'
price = input('How much is a burger? ')
within_budget = float(price) <= 10
is_good_choice = is_answering and within_budget

if is_good_choice:
    print('This restaurant is a great choice!')
else:
    print('Probably not a good idea')

# New code for calculating the meal cost and applying a discount
meal_cost = float(input('What is the total cost of your burger meal: '))
has_discount = input('Do you have a discount? y/n ') == 'y'

if meal_cost > 20 and has_discount:
    meal_cost *= 0.90  # Apply 10% discount
    print('Discount applied')
else:
    print('No discount')

print('Total cost to pay: £{}'.format(format(meal_cost, '.2f')))


# In[ ]:





# ## Elif Statements:

# **elif statement:** used after `if` statements to check whether another condition is `True` or `False`

# In[4]:


dog_size = int(input('How big is the dog? '))

if dog_size > 75:
    print('That is a big dog')
    
elif dog_size < 25:
    print('That is a small dog')
    
else:
    print('That is an average dog')


# You can use multiple `elif` statements `together`

# In[5]:


dog_size = int(input('How big is the dog? '))

if dog_size > 75:
    print('That is a big dog')
    
elif dog_size < 10:
    print('That dog could fit in my pocket')
    
elif dog_size < 25:
    print('That is a small dog')
    
else:
    print('That is an average dog')


# In[ ]:





# ### Exercise 3.5: You're cooking a pizza and need to check that the oven is at the right temperature.

# Write a program to:
# 
# - Ask the user to input the temperature
# - Prints "The oven is too hot" if the temperature is over 200
# - Prints "The oven is too cold" if the temperature is under 150
# - Prints "The oven is at the perfect temperature" if the temperature is 180
# - Prints "The temperature is close enough" for any other temperature

# In[ ]:


# Ask the user to input the temperature
temperature = float(input('Please enter the oven temperature: '))

# Determine the message based on the temperature
if temperature > 200:
    print('The oven is too hot')
elif temperature < 150:
    print('The oven is too cold')
elif temperature == 180:
    print('The oven is at the perfect temperature')
else:
    print('The temperature is close enough')


# In[3]:


temperature = float(input('Please enter the oven temperature: '))

if temperature > 200:
    print('The oven is too hot')
elif temperature < 150:
    print('The oven is too cold')
elif temperature == 180:
    print('The oven is at the perfect temperature')
else:
    print('The temperature is close enough')


# In[ ]:





# ## Random:

# Python has a built-in library for random data

# In[6]:


import random

random_integer = random.randint(1, 100)

print(random_integer)


# The `randint()` function generates a random number between two values

# This program uses `randint()` to simulate dice with any number of sides

# In[11]:


import random

sides = int(input('How many sides does the die have? '))
random_integer = random.randint(1, sides)

print('You rolled a {}'.format(random_integer))


# In[ ]:





# ### Exercise 3.6: This program uses random to simulate a coin flip.

# To finish the program you will need to add the following:
# - If the random coin ip matches the choice input by the user then they win
# - Ohterwise if the random coin ip does not match the choice input by the user then they lose

# In[8]:


import random
def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
        side = 'heads'
    else:
        side = 'tails'
    return side

choice = input('heads or tails: ')
result = flip_coin()

print('The coin landed on {}'.format(result))

# Check if the user's choice matches the result
if choice == result:
    print('You win!')
else:
    print('You lose!')


# ### Exercise 3.7: This program simulates rock, paper, scissors. The first winning condition has been added.
# - To finish the program you'll need to add all of the other winning and losing conditions.

# In[9]:


import random

def random_choice():
    choice_number = random.randint(1, 3)
    
    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'scissors'
    else:
        choice = 'paper'
    return choice

my_choice = input('Choose rock, scissors or paper: ').strip().lower()
opponent_choice = random_choice()

print('Your opponent chose {}'.format(opponent_choice))

if my_choice == opponent_choice:
    print('It\'s a tie!')
elif (my_choice == 'rock' and opponent_choice == 'scissors') or \
     (my_choice == 'scissors' and opponent_choice == 'paper') or \
     (my_choice == 'paper' and opponent_choice == 'rock'):
    print('You win!')
else:
    print('You lose!')


# ### Exercise 3.8: Not Quite Roulette
# 
# #### Ask the user to enter the following three things using input() :
# 1. The amount they want to bet
# 2. A colour (red or black)
# 3. A number between 1 and 100
# 
# #### After generating a random number and colour:
# 1. If the colour matches, the users keeps the amount that was bet
# 2. If the number matches, the users wins double the amount that was bet
# 3. If the colour and number matches, the users wins 100 times the amount that was bet
# 4. When neither the colour or number matches the user wins 0
# 5. Output the amount the user won

# In[12]:


import random

def generate_random_color():
    return 'red' if random.randint(1, 2) == 1 else 'black'

def main():
    # Get user input
    bet_amount = float(input('Enter the amount you want to bet: '))
    user_color = input('Choose a color (red or black): ').strip().lower()
    user_number = int(input('Choose a number between 1 and 100: '))

    # Generate random number and color
    random_number = random.randint(1, 100)
    random_color = generate_random_color()

    print(f'The random number is {random_number}')
    print(f'The random color is {random_color}')

    # Determine the amount won
    amount_won = 0
    if user_color == random_color and user_number == random_number:
        amount_won = 100 * bet_amount
    elif user_number == random_number:
        amount_won = 2 * bet_amount
    elif user_color == random_color:
        amount_won = bet_amount

    # Output the amount won
    print(f'You won {amount_won:.2f}')

if __name__ == '__main__':
    main()


# It can also be written this way:

# In[11]:


import random

def get_random_colour():
    random_number = random.randint(1, 2)
    return 'red' if random_number == 1 else 'black'

def main():
    # Get user inputs
    bet_amount = float(input("Enter the amount you want to bet: "))
    chosen_colour = input("Choose a colour (red or black): ").strip().lower()
    chosen_number = int(input("Choose a number between 1 and 100: "))

    # Generate random outcomes
    random_number = random.randint(1, 100)
    random_colour = get_random_colour()

    # Determine winnings
    winnings = 0

    if chosen_colour == random_colour:
        winnings += bet_amount  # User keeps the amount they bet

    if chosen_number == random_number:
        winnings += 2 * bet_amount  # User wins double the amount they bet

    if chosen_colour == random_colour and chosen_number == random_number:
        winnings = 100 * bet_amount  # User wins 100 times the amount they bet

    # Output the result
    print(f"Random colour: {random_colour}")
    print(f"Random number: {random_number}")
    print(f"You won: ${winnings:.2f}")

if __name__ == "__main__":
    main()


# In[ ]:





# ## Recap:

# This session:
# 1. Comparison operators
# 2. Logical Operators
# 3. If Statements

# Sure, let’s break down each question.
# 
# ### Question 1: Comparison Operators
# 
# In Python, comparison operators are used to compare two values. The `==` operator checks if two values are equal. Here are two more comparison operators:
# 
# 1. **`!=` (Not Equal to)**: This operator checks if two values are not equal.
#    - Example: `5 != 3` evaluates to `True` because 5 is not equal to 3.
# 
# 2. **`<` (Less Than)**: This operator checks if the value on the left is less than the value on the right.
#    - Example: `5 < 10` evaluates to `True` because 5 is less than 10.
# 
# Other comparison operators include `>`, `<=`, and `>=`.
# 
# ### Question 2: Output of Boolean Expressions
# 
# Here’s what each expression evaluates to:
# 
# 1. **`print(True and True)`**
#    - The `and` operator returns `True` if both operands are `True`.
#    - Output: `True`
# 
# 2. **`print(True and False)`**
#    - The `and` operator returns `True` only if both operands are `True`. Here, one operand is `False`.
#    - Output: `False`
# 
# 3. **`print(True or True)`**
#    - The `or` operator returns `True` if at least one operand is `True`.
#    - Output: `True`
# 
# 4. **`print(True or False)`**
#    - The `or` operator returns `True` if at least one operand is `True`. Here, one operand is `False`.
#    - Output: `True`
# 
# ### Question 3: Code Behavior
# 
# Here’s the code with proper indentation and explanation:
# 
# ```python
# apples = 100
# if apples >= 10:
#     print('That is a sensible number of apples')
# elif apples > 50:
#     print('This is too many apples')
# elif apples < 10:
#     print('That is not enough apples')
# ```
# 
# #### Why it Outputs "That is a sensible number of apples":
# 
# The code will output "That is a sensible number of apples" because the condition `apples >= 10` is `True`. 
# 
# **Explanation:**
# - The `if` statement `if apples >= 10:` is checked first. Since `apples` is 100, this condition is `True`. Therefore, the corresponding print statement executes.
# - The `elif` statements are not evaluated because the first `if` condition has already been satisfied. 
# - Thus, "That is a sensible number of apples" is printed, and the other conditions are not checked.
# 
# To fix the code to meet your expected output "This is too many apples", you need to adjust the conditions so that the `elif` for `apples > 50` is checked first:
# 
# ```python
# apples = 100
# if apples > 50:
#     print('This is too many apples')
# elif apples >= 10:
#     print('That is a sensible number of apples')
# elif apples < 10:
#     print('That is not enough apples')
# ```
# 
# In this corrected code:
# - `if apples > 50:` will be `True` for 100, so "This is too many apples" will be printed.

# In[13]:


#### Faulty:
apples = 100
if apples >= 10:
    print('That is a sensible number of apples')
elif apples > 50:
    print('This is too many apples')
elif apples < 10:
    print('That is not enough apples')


# In[14]:


#### Corrected:
apples = 100
if apples > 50:
    print('This is too many apples')
elif apples >= 10:
    print('That is a sensible number of apples')
elif apples < 10:
    print('That is not enough apples')


# In[ ]:




