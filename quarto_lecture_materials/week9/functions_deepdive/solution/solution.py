# Task 1: No Argument, No Return
def greet():
    print("Hello, World!")

# Task 2: Single Argument, No Return
def display(value):
    print(value)

# Task 3: Multiple Arguments, No Return
def show_sum(a, b):
    print(a + b)

# Task 4: No Argument, With Return
def get_pi():
    return 3.14159

# Task 5: Single Argument, With Return
def square(x):
    return x * x

# Task 6: Multiple Arguments, With Return
def find_max(a, b, c):
    return max(a, b, c)

# Task 7: Default Arguments
def power(base, exponent=2):
    return base ** exponent

# Task 8: Variable Number of Arguments
def calculate_mean(*args):
    if len(args) == 0:
        return "Error: No values provided"
    return sum(args) / len(args)

# Task 9: Keyword Arguments
def create_profile(name, **kwargs):
    print(f"Name: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usages:
greet()  # Output: Hello, World!
display("Hello!")  # Output: Hello!
show_sum(3, 4)  # Output: 7
print(get_pi())  # Output: 3.14159
print(square(4))  # Output: 16
print(find_max(3, 5, 4))  # Output: 5
print(power(3))  # Output: 9
print(power(3, 3))  # Output: 27
print(calculate_mean(1, 2, 3, 4, 5))  # Output: 3.0
print(calculate_mean())  # Output: Error: No values provided
create_profile("Alice", age=25, location="USA")  # Output: Name: Alice \n age: 25 \n location: USA
