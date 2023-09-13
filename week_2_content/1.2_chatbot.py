# Chatbot with conditional logic
# Author: Nick Vincent
# Date: Sep 11, 2023

# Description: This bot will ask questions
# and take the user's answer into account when
# responding

# === Algorithm ===
# Ask user how it's going
# Get response
# If they said "Good", respond "Good!"
# Otherwise, if they said Bad, then reply "Oh no!"

#%%
print("How's it going?")
reply = input()

# Note the Double Equal sign
# Note the indentation
if reply == "Good":
    print("Good")

elif reply == "Bad": # elif is short for else if
    print("Oh no!")
else:
    print("I see...")


#%%
print("How's it going?")
reply = input()

# Example of using "or"
if reply == "Good" or reply == "good" or reply == "Great":
    print("Good")

elif reply == "Bad": # elif is short for else if
    print("Oh no!")
else:
    print("I see...")