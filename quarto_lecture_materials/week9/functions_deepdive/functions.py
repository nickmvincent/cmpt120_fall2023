# Try to get this code to run by ONLY ADDING things

# give this a default argument
def f1(x):
    return x * 2

# takes multiple arguments: pass then below
def f2(a, b):
    return a + b

# f3 takes no arguments
def f3():  # No arguments
    return "Hello!"

def f4(value):  # Single argument
    if value > 0:
        return "Positive"
    else:
        return "Non-positive"


successes = []
try:
    r1 = f1()
    successes.append("f1 works")
except Exception as e:
    print(e)

try:
    r2 = f2()
    successes.append("f2 works")

except Exception as e:
    print(e)

try:
    r3 = f3("a")
    successes.append("f3 works")

except Exception as e:
    print(e)

try:
    r4 = f4()
    successes.append("f4 works")

except Exception as e:
    print(e)

for success in successes:
    print(success)