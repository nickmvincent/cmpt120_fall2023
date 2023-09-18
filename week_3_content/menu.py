#%%
item1 = "laksa"
item2 = "chicken rice"
item3 = "mee siam"
item4 = "sushi platter"
item5 = "sushi deluxe"
item6 = "sushi supreme"

print(item1)
print(item2)
print(item3)
print(item4)
print(item5)
print(item6)

#%%
items = [item1, item2, item3, item4, item5, item6]

for item in items:
    print(item)

#%%
# loops are nice to make things fancy without repeating ourselves
for item in items:
    print('**', item, '**')


#%%
for number in range(0,10):
    print(number)

# %%
for index in range(0, 6):
    print(items[index])
# %%
