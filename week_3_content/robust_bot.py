
# === FIRST VERSION: Using .strip()

#%%
# Ask user how it's going and make a comment

print("How's it going?")
reply = input()

if reply == "Good":
    print("I'm glad you're good!")
    print("What's something good that happened?")
    good_thing = input()
    print(good_thing.strip(".") + "? That's great.")



# %%
# === SECOND VERSION: Using .lower()
# Ask user how it's going and make a comment
print("How's it going?")
reply = input()

if reply.lower() == "good":  # or: reply.upper() == "GOOD"
    print("I'm glad you're good!")
    print("What's something good that happened?")
    good_thing = input()
    print(good_thing.strip(".") + "? That's great.")

#%% 
# === CHAINING EXAMPLE ===
reply = input()

reply_all_lowercase = reply.lower()

reply_all_lower_case_stripped = reply_all_lowercase.strip("!,.?")

print(reply_all_lower_case_stripped)

print(reply.lower().strip("!,.?"))

print(
    reply_all_lower_case_stripped == reply.lower().strip("!,.?")
)
# %%
# === the in keyword ===
print("Enter year you were born")
year = input.strip(" ,!.")
pig_years = ["1935, 1947, 1959, 1971", "1983", "1995", "2007"]

# use the in keyword to check for "inclusion"
if year in pig_years:
    print("You are a lucky pig!")
else:
    print("I only have pig years memorized right now :(")

#%%
# === What the in keyword saves us from ===
# What we could have done instead...
if year == "1935" or year == "1947" or year == "1959": # etc etc
    print("You are a lucky pig!")

#%%
# Using the in keyword to check if a string is in 
# another string
reply = "good"
print(reply in "I'm good")

reply = input("How are you?").lower()
if "good" in reply:
    print("I'm glad you said the word 'good'!")


#%%
# === FOOD BOT PSEUDO CODE

# Description: A bot to ask about my favorite food
# It will suggest restaurants in Vancouver based on my answer.

# Algorithm:
# Define several food categories as lists of foods
# e.g. japanese = ["sushi", "tempura"]
# singaporean = ["laksa", "chicken rice"]
# Ask the user for a favorite dish, e.g. laksa
# Get the dish name
# Check if the dish is in any categories
# If so, suggest a restaurant of that category
