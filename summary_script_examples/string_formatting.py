# String Formatting in Python

# Using Variables
name = "Alice"
age = 30

# 1. Using String Concatenation:
print("Method 1: String Concatenation")
print("Hello, " + name + "! You are " + str(age) + " years old.")
print("----------------------")

# 2. Using print() with Multiple Arguments:
print("Method 2: print() with Multiple Arguments")
print("Hello, ", name, "! You are ", age, " years old.", sep="")
print("----------------------")

# 3. Using %-formatting:
print("Method 3: %-formatting")
print("Hello, %s! You are %d years old." % (name, age))
print("----------------------")

# 4. Using str.format():
print("Method 4: str.format()")
print("Hello, {}! You are {} years old.".format(name, age))
# Named placeholders
print("Hello, {name}! You are {age} years old.".format(name=name, age=age))
# Indexing in placeholders
print("Hello, {1}! You are {0} years old.".format(age, name))
print("----------------------")

# 5. Using f-strings (formatted string literals) - Available in Python 3.6+
print("Method 5: f-strings")
print(f"Hello, {name}! You are {age} years old.")
# Expressions inside f-string
print(f"{name}'s age next year will be {age + 1}.")
print("----------------------")

# 6. Using Template Strings:
from string import Template
print("Method 6: Template Strings")
template = Template("Hello, $name! You are $age years old.")
print(template.substitute(name=name, age=age))
print("----------------------")