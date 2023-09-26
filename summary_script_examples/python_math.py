# Define some numbers to work with
a = 5
b = 3

# 1. ** Exponentiation operator
# This raises the first number to the power of the second.
result_exponent = a ** b
print(f"{a} raised to the power of {b} is: {result_exponent}")  # Outputs: 5 raised to the power of 3 is: 125

# 2. * Multiplication operator
result_multiply = a * b
print(f"{a} multiplied by {b} is: {result_multiply}")  # Outputs: 5 multiplied by 3 is: 15

# 3. - Subtraction operator
result_subtract = a - b
print(f"{a} minus {b} is: {result_subtract}")  # Outputs: 5 minus 3 is: 2

# 4. + Addition operator
result_add = a + b
print(f"{a} plus {b} is: {result_add}")  # Outputs: 5 plus 3 is: 8

# 5. / Division operator
# This performs floating point division.
result_divide = a / b
print(f"{a} divided by {b} is: {result_divide}")  # Outputs: 5 divided by 3 is: 1.6666666666666667

# 6. // Floor Division operator
# This performs division and returns the largest whole number result.
result_floor_divide = a // b
print(f"{a} floor-divided by {b} is: {result_floor_divide}")  # Outputs: 5 floor-divided by 3 is: 1

# 7. % Modulus operator
# This returns the remainder when the first number is divided by the second.
result_modulus = a % b
print(f"The remainder when {a} is divided by {b} is: {result_modulus}")  # Outputs: The remainder when 5 is divided by 3 is: 2
