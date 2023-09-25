#%%
# === This is a scratchpad for live coding during Week 4 ===
#%%
print("hello, week4")

#%%


#%%
for i in [10,9,8,7,6,5,4,3,2,1,0]:
    print(i)
# %%
for i in range(10,-1,-1):
    print(i)
# %%
for i in reversed(range(0,11,1)):
    print(i)
# %%
for i in range(0,5,1):
    print(i)
# %%
help(range)
# %%
spicy = "yes"
meat = "yes"

if spicy == "yes" and meat == "yes":
    print("Go to Spicy Meat Land")
else:
    print("Go to Many Options World")
# %%
"?.!hello".strip("?.h")
# %%
"?.!hello".strip("?.!h")
# %%
"hello".replace("ello", "allo")

# %%
"ABC".strip("B")
# %%
"ABC".strip("AB")
# %%
"ABCD".strip("B")
# %%
"ABCD".strip("A")
# %%
"      asdA  a a sd asd asd as dsa        "

#%%
for i in [1,2,3]:
    for j in [4,5,6]:
        result = i * j
        print("  ", i, j, result)
        
    print(i, j, result)
# %%
starbucks_vote = 0
tims_votes = 0
other_votes = 0

print("Please give one of the following answers:")
print("starbucks, tim hortons, or anything else")

for i in range(5):
    # choice = "starbucks"
    choice = input()

    if choice.lower() == "starbucks":
        starbucks_vote = starbucks_vote + 1
    elif choice.lower() == "tim hortons":
        tims_votes = tims_votes + 1
    else:
        other_votes = other_votes + 1


print(starbucks_vote)
print(tims_votes)
print(other_votes)

if starbucks_vote > tims_votes:
    print("Starbucks wins")
# %%
print("Asd" + 1)
# %%
