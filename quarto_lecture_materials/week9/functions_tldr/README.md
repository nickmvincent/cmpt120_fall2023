# Basic intro to functions in Python!


## Definition
From the docs:

"The keyword def introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next line, and must be indented."


Example: 

```
def my_math_function(a, b):
    return a*2 + b*3
```


## Recipe for a function

start with `def` + `function_name` + arguments in parentheses + a colon

`def my_math_function(a, b)`

All indented code after the def line is part of the function

At the end of your function (or sometimes, in the middle), you use `return` to send back a return value
`return a*2 + b*3`


## Some examples
```
def greet(name):
    message = f"Hello, {name}!"
    return message

# Usage:
result = greet("Alice")
print(result)  # Output: Hello, Alice!
```

- "greet" function takes a single argument (`name`), constructs a greeting message (using f string), and returns it. When called with the argument "Alice", it returns the string "Hello, Alice!".




## Scopes
Functions have their own scope

You must define the variables you want to use in the function, or pass them as arguments

Helpful to imagine your function being *code in a different file*



## Default arguments

def power(base, exponent=2):
    result = base ** exponent
    return result

# Usage:

```
result1 = power(3)  # Using default exponent value 2
result2 = power(3, 3)  # Specifying exponent value 3
print(result1)  # Output: 9
print(result2)  # Output: 27
```

In this example, the power function has a default argument for exponent. If exponent is not provided when calling the function, it defaults to 2. The function calculates the power of base raised to exponent and returns the result.
