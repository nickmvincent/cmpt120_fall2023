# Set a sample value
value = 10

# 1. if statement only
print("1. if statement only")
if value == 10:
    print("Value is 10")
print("----------------------")

# 2. if-else statement
print("2. if-else statement")
if value < 10:
    print("Value is less than 10")
else:
    print("Value is 10 or greater")
print("----------------------")

# 3. if-elif statement (without else)
print("3. if-elif statement (without else)")
if value < 5:
    print("Value is less than 5")
elif value < 10:
    print("Value is less than 10 but greater than or equal to 5")
elif value == 10:
    print("Value is 10")
print("----------------------")

# 4. if-elif-else statement
print("4. if-elif-else statement")
if value < 5:
    print("Value is less than 5")
elif value < 10:
    print("Value is less than 10 but greater than or equal to 5")
else:
    print("Value is 10 or greater")
print("----------------------")

# 5. Multiple elifs (showcasing more than one elif)
print("5. Multiple elifs")
if value < 3:
    print("Value is less than 3")
elif value < 6:
    print("Value is less than 6 but greater than or equal to 3")
elif value < 9:
    print("Value is less than 9 but greater than or equal to 6")
else:
    print("Value is 9 or greater")
print("----------------------")
