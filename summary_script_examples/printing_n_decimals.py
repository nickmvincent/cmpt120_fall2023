# First, let's define a floating point number.
float_number = 123.456789

# 1. Using the round() function:
# The round() function can be used to round a float to the given number of decimal places.
rounded_number = round(float_number, 2)  # This rounds to 2 decimal places.
print("Using round():", rounded_number)

# Note: While round() is useful, it may not always produce the exact string representation you want in all scenarios.

# 2. Using formatted string literals (f-strings, Python 3.6+):
# The format specification in f-strings allows you to specify the number of decimal places.
print(f"Using f-string: {float_number:.2f}")  # .2f means 2 decimal places.

# 3. Using the str.format() method:
# This method provides a way to format strings by replacing placeholders with values.
print("Using str.format(): {:.2f}".format(float_number))

# 4. Using the % operator (older way, but still seen in legacy code):
# This is a C-style way to format strings in Python.
print("Using %% operator: %.2f" % float_number)