#%%
print("Hello world")
# %%
my_list = [1,2,3]

#%%
x = 4
y = 5

#%%
my_list.append(x)
print(my_list)

# %%
[1,2,3] + [4]
#%%
help(range)

# %%
print(list(range(5)))

#%%
print(list(range(1, 6)))

# %%
print(list(range(0, 2, 2)))
# %%
print(list(range(0, 3, 2)))
# %%
print(list(range(0, 4, 2)))

#%%
words = ["tickle", "pop", "roll", "dance"] 
output = ""
for word in words:
    output = output + word[len(words)-2]
print(output)

# %%

with open('words.csv', 'r') as file:
    for line in file:
        words = line.strip().split(',')

        string_to_print = "*"
        for word in words:
            first_letter = word[0]
            first_letter_as_lower = first_letter.lower()
            string_to_print += first_letter_as_lower
    print(string_to_print)
# %%


x = "1 2 3"

#%%
x.split(" ")
# %%
x.split()
# %%