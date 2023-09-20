# === Week 3-3 Running Example ===
# Let's try to use all the Python
# keywords and concepts we've learned

#%%
# We've seen a lot of strings

print("This is a single .py file that aims to use all our keywords and concepts so far!")
# This is a comment

print("This is how we print", "using a common to separate two arguments")
print("This is how we print" + " using concatenation" + " (note the spaces)")

# define a variable named my_string. assign it the value "this is a string"
my_string = "this is a string" 

my_multi_line_string = """
This is a multi-line string
"""

# we can make a string with single quotes too. have to be consistent, though!
my_string_with_single_quotes = 'my string'

my_list = ["item1", "item2"]

# normally, we put this at the top
import random
print(
    random.choice(my_list)
)

print("Pick an option: A, B, or C (it's ok if it's lowercase and has whitespace)")
user_pick = input()
user_pick_processed = user_pick.strip().upper()

if user_pick_processed == "A":
    print("A")
elif user_pick_processed == "B":
    print("B")
elif user_pick_processed == "C":
    print("C")
else:
    print("You didn't pick one of the options!")

# Compare numbers
