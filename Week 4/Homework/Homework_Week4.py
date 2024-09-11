#!/usr/bin/env python
# coding: utf-8

# # Homework, Session 4

# ### Question 1:
# 
# **I have a list of things I need to buy from my supermarket of choice.**

# In[1]:


shopping_list = [ 
"oranges", 
"cat food", 
"sponge cake", 
"long-grain rice", 
"cheese board", 
] 
print(shopping_list[1]) 


# 1. I want to know what the first thing I need to buy is. However, when I run the program it shows me a different answer to what I was expecting? 
# 2. What is the mistake? 
# 3. How do I fix it? 

# The mistake in the program is that we're trying to print the first item in the `shopping_list`, but we're actually printing the second item instead.
# 
# ### Explanation:
# 
# In Python, list indexing starts from `0`, which means:
# 
# - `shopping_list[0]` refers to the first item in the list.
# - `shopping_list[1]` refers to the second item in the list.
# 
# ### Current Code:
# 
# ```python
# shopping_list = [
#     "oranges", 
#     "cat food", 
#     "sponge cake", 
#     "long-grain rice", 
#     "cheese board",
# ] 
# 
# print(shopping_list[1])  # This prints "cat food"
# ```
# 
# The code `print(shopping_list[1])` prints "cat food" because it's the second item in the list.
# 
# ### Solution:
# 
# To print the **first** item in the list, we should use `shopping_list[0]`.
# 
# ### Corrected Code:
# 
# ```python
# shopping_list = [
#     "oranges", 
#     "cat food", 
#     "sponge cake", 
#     "long-grain rice", 
#     "cheese board",
# ] 
# 
# print(shopping_list[0])  # This will print "oranges"
# ```
# 
# This will correctly print "oranges", which is the first item in the `shopping_list`.

# In[2]:


shopping_list = [
    "oranges", 
    "cat food", 
    "sponge cake", 
    "long-grain rice", 
    "cheese board",
] 

print(shopping_list[0])  # This will print "oranges"


# In[ ]:





# ### Question 2:
# 
# **I'm setting up my own market stall to sell chocolates. I need a basic till to check the prices of different chocolates that I sell.**
# 
# **I've started the program and included the chocolates and their prices. Finish the program by asking the user to input an item and then output its price.**

# In[ ]:


chocolates = { 
'white': 1.50, 
'milk': 1.20, 
'dark': 1.80, 
'vegan': 2.00, 

# Current Unfinished Code


# In[3]:


chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

item = input("Enter the type of chocolate: ")
print(chocolates.get(item, "Item not found"))

# Corrected and finished code


# In[ ]:





# ### Question 3:
# 
# **Write a program that simulates a lottery. The program should have a list of seven numbers that represent a lottery ticket. It should then generate seven random numbers.**
# 
# **After comparing the two sets of numbers, the program should output a prize based on the number of matches:**
# - £20 for three matching numbers 
# - £40 for four matching numbers 
# - £100 for five matching numbers 
# - £10000 for six matching numbers 
# - £1000000 for seven matching numbers

# In[19]:


import random

ticket = [3, 12, 19, 23, 36, 42, 49]
lottery_numbers = random.sample(range(1, 50), 7)

# Print lottery numbers to verify randomness
print("Your ticket numbers:", ticket)
print("Generated lottery numbers:", lottery_numbers)

matches = len(set(ticket) & set(lottery_numbers))

if matches == 3:
    print("£20")
elif matches == 4:
    print("£40")
elif matches == 5:
    print("£100")
elif matches == 6:
    print("£10000")
elif matches == 7:
    print("£1000000")
else:
    print("No prize")


# In[17]:


import random

def generate_lottery_numbers():
    # Generate 7 unique random numbers between 1 and 49 for the lottery draw
    return random.sample(range(1, 50), 7)

def calculate_prize(matches):
    # Define the prize based on the number of matches
    prize_dict = {
        3: 20,
        4: 40,
        5: 100,
        6: 10000,
        7: 1000000
    }
    # Return the corresponding prize or 0 if less than 3 matches
    return prize_dict.get(matches, 0)

def main():
    # A sample ticket for the user with 7 unique numbers between 1 and 49
    user_ticket = [5, 12, 19, 26, 33, 40, 47]
    
    # Generate 7 random numbers for the lottery
    lottery_numbers = generate_lottery_numbers()
    
    # Determine the number of matching numbers between user ticket and lottery numbers
    matches = len(set(user_ticket) & set(lottery_numbers))
    
    # Calculate the prize
    prize = calculate_prize(matches)
    
    # Output the results
    print(f"Your ticket numbers: {user_ticket}")
    print(f"Lottery numbers: {lottery_numbers}")
    print(f"Number of matches: {matches}")
    if prize > 0:
        print(f"Congratulations! You have won £{prize}.")
    else:
        print("Sorry, you didn't win this time.")

# Run the lottery simulation
if __name__ == "__main__":
    main()


# In[20]:


# Both codes above shows the same result.


# In[ ]:




