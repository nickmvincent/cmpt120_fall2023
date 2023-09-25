# Example: Printing a multiplication table

# Using nested for loops to generate a multiplication table for numbers 1 through 5
print("Multiplication Table (1 to 5):")
for i in range(1, 6):  # Outer loop, iterating over numbers 1 to 5
    for j in range(1, 6):  # Inner loop, iterating over numbers 1 to 5 for each iteration of the outer loop
        print(i * j, end='\t')  # Multiply the numbers and print the result, followed by a tab
    print()  # Move to the next line after each row

# Explanation:
# For every iteration of the outer loop (i.e., for each value of 'i'),
# the inner loop runs completely, iterating over its own set of values (for each value of 'j').
# As a result, for each 'i', every possible 'j' value is paired with it once.
