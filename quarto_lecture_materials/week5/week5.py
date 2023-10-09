# %% [markdown]
# ## Quick note for those reading slides
# There's only one set of slide for week 5 (Monday was a holiday).
# 
# ## 5-1 Housekeeping
# 
# - Updates on marking
# - Updates on additional study materials (and how to get feedback)
# - Office hours today
# 
# ## 5-1 agenda
# 
# - Quick set of review questions
# - Quick review on accumulator pattern
# - Completing our recommender system example
#   - Putting together for loops, nested for loops, list slicing, string slicing
# 
# 
# ## Review questions
# 
# ## Question 1a
# What does this snippet output?

# %%
#| echo: true
response = "I LOVE RAIN!!"
words = response.lower().strip("!").split(" ")
if "rain" in words or "umbrella" in words:
    print("You're a fan of the rain?")

# %% [markdown]
# ## Question 1b

# %%
#| echo: true
response = "I LOVE RAIN!!"
try:
    words = response.lower().split(" ").strip("!")
    if "rain" in words or "umbrella" in words:
        print("You're a fan of the rain?")
except AttributeError:
    print("Something went wrong")

# %% [markdown]
# ## Question 2a
# What does this output?

# %%
#| echo: true
fruits = "durian, rambutan, lychee"
fruit_list = fruits.split(",")
print("durian" in fruit_list)
print("rambutan" in fruit_list)

# %% [markdown]
# ## Question 2b
# What does this output?

# %%
#| echo: true
fruits = "durian,rambutan,lychee".split(",")
print(fruits[1][0].upper())

# %% [markdown]
# ## Question 3
# Find three errors with this code:
# 
# ```{.python}
# z = int(input["Give me a number, any number: "])
# if z > 5 and <= 10:
# 	print(x)
# ```
# 
# ## Question 3 -- answer
# ```{.python}
# z = int(input("Give me a number, any number: "))
# if z > 5 and z <= 10:
# 	print(z)
# ```
# 
# 
# ## Question 4
# What does this snippet output?

# %%
#| echo: true
letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(len(letters))

print(letters[1:3])
print(letters[:4])
print(letters[3:])
print(letters[:])
print(letters[-1])
print(letters[3:-1])

# %% [markdown]
# ## Trick to remember slicing
# 
# `letters[:4]` will give you 4 total items in your output! It must start at 0... hence you get 0,1,2, and 3.
# 
# ## Accessing characters in strings
# - Just like accessing items in a list
# - If you think of strings as a list of characters, you're good to go
# - (As long as you know how lists work)
# 
# ## Accumulator review
# "Go through all the items in a pile and pick out the red ones"

# %%
#| echo: true
items = ["red", "blue", "red", "green"]
items_we_grab = []
for item in items:
    if item == "red":
        items_we_grab += [item]
print(items_we_grab)

# %% [markdown]
# ## Week 5 Learning Objective
# 
# 
# ## Open + read lines from a file

# %%
#| echo: true
with open('fake_data.csv', 'r') as file:
    lines = file.readlines()
    print(len(lines))

# %% [markdown]
# ## Split a string into a list

# %%
#| echo: true
text = "Python is fun"
words = text.split()  # ['Python', 'is', 'fun']
print(words)

# %% [markdown]
# ## Access specific elements of a list using indexing/slicing

# %%
#| echo: true
numbers = [1, 2, 3, 4, 5]
first_element = numbers[0]    # 1
sliced_elements = numbers[1:4]  # [2, 3, 4]

# %% [markdown]
# ## Access specific character in a string using indexing/slicing

# %%
#| echo: true
text = "Hello World"
first_char = text[0]  # 'H'
sliced_chars = text[6:11]  # 'World'

# %% [markdown]
# ## Perform comparisons between numbers, taking into account order of operators (operator precedence)

# %%
#| echo: true
result = 2 + 3 * 4 > 10  # Evaluates to 2 + 12 > 10 => 14 > 10 => True
print(result)

# %% [markdown]
# ## Perform comparisons (e.g. !=, <,>) with strings

# %%
#| echo: true
string1 = "apple"
string2 = "banana"
print(string1 != string2)  # True
print(string1 < string2)   # True, because 'a' comes before 'b' alphabetically

# %% [markdown]
# ## Interpret code with nested conditionals + comparison operators (e.g. !=, <,>=)

# %%
#| echo: true
x = 5
y = 10
if x != y:
    if x < y:
        print("x is less than y")
    else:
        print("x is greater than y")
else:
    print("x is equal to y")

# %% [markdown]
# ## Find the common elements between 2 lists

# %%
#| echo: true
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = []
for x in list1:
    if x in list2:
        common_elements.append(x)
print(common_elements)  # [3, 4]

# %% [markdown]
# ## Understand + use nested for loops

# %%
#| echo: true
for i in range(3):
    for j in range(2):
        print(i, j)

# %% [markdown]
# ## Apply operator order to evaluate expressions

# %%
#| echo: true
result = 3 + 4 * 2 / (1 - 5)  # Evaluates using operator precedence: multiplication, division, subtraction, addition
print(result)

# %% [markdown]
# ## Concatenate lists

# %%
#| echo: true
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)  # [1, 2, 3, 4, 5, 6]

# %% [markdown]
# ## Apply accumulation pattern for strings and lists (previously was numbers)

# %%
#| echo: true

# For strings
words = ["Hello", "World"]
sentence = ""
for word in words:
    sentence += word + " "
print(sentence.strip())  # Hello World

# For lists
matrix = [[1, 2], [3, 4]]
flat_list = []
for sublist in matrix:
    for item in sublist:
        flat_list.append(item)
print(flat_list)  # [1, 2, 3, 4]

# %% [markdown]
# ## Calculate the maximum among several values

# %%
#| echo: true

values = [3, 5, 2, 8, 6]
maximum = values[0]
for value in values:
    if value > maximum:
        maximum = value
print(maximum)  # 8

# %% [markdown]
# ## Ok, back to content
# 
# - We want to extend our recommender systems example
# 
# ## Let's recap...
# 
# ```{.python}
# with open("example.csv", "r") as file:
#     # Skip header
#     header = file.readline()
#     
#     # Process and print each record
#     for line in file:
#         columns = line.strip().split(",")
#         nice_output = ""
#         for column in columns:
#           nice_output += column + " | "
#         print(nice_output)
# ```
# 
# 
# ## Generating data (advanced)

# %%
#| echo: true

import csv
import random

# Lists of names and diets
names = ["Michael Jordan", "Tom Hanks", "Arya Stark", "Goku", "Scarlett Johansson", 
         "Mickey Mouse", "Hermione Granger", "Naruto", "Serena Williams", "Oprah Winfrey",
         "Leonardo DiCaprio", "Mario", "Taylor Swift", "Darth Vader", "James Bond",
         "Usain Bolt", "Tony Stark", "Bugs Bunny", "The Rock", "Walter White",
         "Sheldon Cooper", "Mulan", "Elsa", "Sherlock Holmes", "Jack Sparrow",
         "Luffy", "Luke Skywalker", "Marilyn Monroe", "Freddie Mercury", "Lady Gaga",
         "Superman", "Wonder Woman", "Neo", "Beyonce", "Ash Ketchum",
         "Lara Croft", "Elvis Presley", "Kermit the Frog", "Spider-Man", "Hannibal Lecter",
         "Indiana Jones", "Simba", "Rihanna", "Dexter Morgan", "Morpheus",
         "Wolverine", "Cinderella", "Captain America", "Thor", "Katniss Everdeen"]

movies_by_genre = {
    "Drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather", "Titanic", "Fight Club"],
    "Action": ["The Dark Knight", "Avengers: Endgame", "Pulp Fiction", "Jurassic Park", "Lord of the Rings: The Fellowship of the Ring"],
    "Sci-Fi": ["Inception", "The Matrix", "Back to the Future", "Star Wars: Episode IV", "Blade Runner"],
    "Animation": ["The Lion King", "Toy Story", "Frozen", "Finding Nemo", "Shrek"],
    "Classic": ["Casablanca", "Jaws", "Gone with the Wind", "Psycho", "Citizen Kane"]
}

parties = ["very left wing", "left wing", "right wing", "very right wing"]

diets = ["plant-heavy", "meat-heavy", "fruit-heavy", "balanced", "dairy-heavy"]

# Generate 50 records
records = [["name", "favorite_movie", "second_favorite_movie", "preferred_political_party", "ideal_diet"]]
for _ in range(50):
    name = random.choice(names)
    genre = random.choice(list(movies_by_genre.keys()))
    movie = random.choice(movies_by_genre[genre])
    movie2 = random.choice(movies_by_genre[genre])
    party = random.choice(parties)
    diet = random.choice(diets)
    records.append([name, movie, movie2, party, diet])

# Write to a CSV file
with open("fake_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(records)

# Display the first few rows
for row in records[:3]:
    print(", ".join(row))

# %% [markdown]
# ## Get your own fake_data.csv
# 
# - Download csv file from Canvas -> GitHub
# - Download python file from Canvas -> GitHub and run it
# - Bonus question: what will be different?
# 
# ## Check that you can read it

# %%
#| echo: true
with open("fake_data.csv", "r") as file:
    header = file.readline()   
    print(header)
    line = file.readline()
    print(line) 

# %% [markdown]
# ## Similarity
# 
# Our initial definition definition: "common interests counter"
# 
# - If we have the same favorite movie, that's one common interest
# - If we have the same preferred political party, that's one common interest.
# - If we also have the same preferred diet, that's one common interest.
# - Let's see who is the most similar!
# 
# 
# ## Many definitions of similar
# 
# In CS and math, there are many ways we can see how "similar" or "close" two items are
# 
# - (cosine distance, manhattan distance, etc.)
# - So we need to specify a definition and algorithm
# 
# ## Our movie/political party/diet recommender system
# 
# To recommend a movie to someone, we take the following approach:
# 
# - We'll look at favorite movie, preferred political party, and ideal diet
# - Each match counts as one similarity score. So score between any two people ranges from 0 to 3.
# - When we find the "highest" score, suggest our user watch that person's second favorite movie!
# 
# ## Our algorithm
# 
# ### Initalize
# - Set variables to hold all the things we need (i.e., get our buckets ready)
# 
# ### Loop
# - Run through every record and process it
# 
# ## Initialize
# - Pick the user we'll give a recommendation to
# - Define a variable to hold similarity score (starts at zero)
# - Define a variable to keep track of which person is most similar
# - Define a variable to keep track of what what we'll recommend
# 
# ## Loop
# 
# ### For each person other than our chosen one
# - Compare the two people
# - Check if favorite movie is the same. if so, add one similarity score
# - Check if preferred political party is the same.  if so, add one similarity score
# - Check if ideal diet is the same. if so, add one similarity score
# - If similarity score is higher than the current top score, update top score/recommendation
# 
# Note: we'll have to use our list/string indexing carefully!
# 
# ## Our pseudo code

# %%
#| echo: true

# select a user (who will receive recommendation)
# init variables to hold top similarity score, top person, recommendation

# load data
    # use a loop to go through all other record lines (one record = one user)
    # make sure to skip chosen user
    # split each record line into a list of items
        # use a nested loop to go through each item
        # make sure we compare columns correctly
    # check if similarity score is higher
        # update if so

# print top score, record, and recommendation

# %% [markdown]
# ## Initialize

# %%
#| echo: true
# select a user + init variables to keep track of scores
index_of_user = 17
top_score = 0
top_record = ""
recommendation = ""

# load data
    # use a loop to go through all other record lines (one record = one user)
    # make sure to skip chosen user
    # split each record line into a list of items
        # use a nested loop to go through each item
        # make sure we compare columns correctly
    # check if similarity score is higher
        # update if so

# print top score, record, and recommendation

# %% [markdown]
# ## Load data

# %%
#| echo: true
# select a user + init variables to keep track of scores
index_of_user = 17
top_score = 0
top_record = ""
recommendation = ""

# load data
with open("fake_data.csv", "r") as file:
    # Skip header
    header = file.readline()
    print(header)
    # use a loop to go through all other record lines (one record = one user)
    # make sure to skip chosen user
    # split each record line into a list of items
        # use a nested loop to go through each item
        # make sure we compare columns correctly
    # check if similarity score is higher
        # update if so

# print top score, record, and recommendation

# %% [markdown]
# ## First for loop

# %%
#| echo: true
# select a user + init variables to keep track of scores
index_of_user = 17
top_score = 0
top_record = ""
recommendation = ""

# load data
with open("fake_data.csv", "r") as file:
    # Skip header
    all_lines = file.readlines()
    header = all_lines[0]
    records = all_lines[1:]

    user_record = records[index_of_user]

    # use a loop to go through all other record lines (one record = one user)
    for record in records:
        if line == user_record:
            continue

        # split each record line into a list of items
        columns = record.strip().split(",")
        print(columns)
        # use a nested loop to go through each item

# %% [markdown]
# ## Note on printing as we go
# 
# As we write this code, at each step let's make our code print something out so we know we're making progress!
# 
# When you're feeling stuck, trying printing something for every new line of code you write.
# 
# 
# ##
# ![How to draw an owl dot jpeg](owl.jpg)
# 
# 
# ## Nested loop

# %%
#| echo: true
# select a user + init variables to keep track of scores
index_of_user = 17
top_score = 0
top_record = ""
recommendation = ""

# load data
with open("fake_data.csv", "r") as file:
    all_lines = file.readlines()
    header = all_lines[0]
    records = all_lines[1:]

    user_record = records[index_of_user].strip().split(",")

    # use a loop to go through all other record lines (one record = one user)
    for record in records:
        columns = record.strip().split(",")

        if user_record[0] == columns[0]:
            print("Skipping ", record)
            continue

        score_for_current_record = 0
        # split each record line into a list of items
        
        # use a nested loop to go through each item
        # use manually defined [1,3,4,5] to get only
        # favorite_movie, party, diet (skip)
        for column_index in [1,3,4]:
            if columns[column_index] == user_record[column_index]:
                score_for_current_record += 1
        
        if score_for_current_record > top_score:
            top_score = score_for_current_record
            top_record = record
            recommendation = columns[2]

print("You are", user_record)

print("After careful consideration, we have found that the most similar user is")
print(top_record)
print(f"You have a similarity score of {top_score}")

print("We recommend you watch", recommendation)

# %% [markdown]
# ## Ok, let's take a step back
# 
# - switch to live coding here


