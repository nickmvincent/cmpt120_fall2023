# Chatbot
# Author: Nick Vincent
# Date: Sep 11, 2023

# === Algorithm ===
# Print out a greeting
# Get the user's name from input
# Respond nicely

#%%
# Print out a greeting
print("Hi, what's your name")

# Get the user's name from input
name = input()
# name = input("Hi, what's your name?")

# Respond nicely
print("Nice to meet you " + name)

#%%
# Ask for user's favorite book
# Let the user respond
# Make a comment about it
print("What is your favorite book?")
input()
print("Wow, very cool.")



# === Goal ===
# Select a comment randomly from a list
# so that the comments aren't too repetitive!

# === Algorithm as "pseudo code" ===
# Define a list of possible comments
# Choose one randomly
# Print the chosen comment


#%%
import random

print("Hi, what's your name")
name = input()
print("Nice to meet you, " + name)

# Ask for user's favorite book and let them respond
print("What is your favorite book?")
input()

# Define a list of possible comments
comment_choices = [
    "Nice!",
    "That's a good one.",
    "That's profound",
    "Wow, you must be quite a well-read person!",
    "Lol, really?"
]

# Choose one randomly
random_comment = random.choice(comment_choices)

# Print the chosen comment
print(random_comment)



# %%