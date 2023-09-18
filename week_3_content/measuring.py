#%%
# === First version: Measuring things in Canada ===
print("I'll tell you about measurements in Canada")

measure = input(
    "What are you measuring (mass or volume)").lower().strip(".!")

if measure == "mass":
    is_weight = input("Is it your weight (yes or no)").lower()
    if is_weight == "yes":
        print("lbs")
    else:
        print("kg")


elif measure == "volume":
    # TODO: add this branch
    pass

#%%
# === Second version: Measuring things in Canada ===
print("I'll tell you about measurements in Canada")

measure = input(
    "What are you measuring (mass or volume)").lower().strip(".!")

if measure == "mass":
    is_weight = input("Is it your weight (yes or no)").lower()
    if is_weight == "yes":
        print("lbs")
    else:
        print("kg")


elif measure == "volume":
    is_cooking = input("Is it for cooking (yes or no)").lower()
    if is_cooking == "yes":
        print("Use cups and spoons")
    else:
        print("Use metric")
