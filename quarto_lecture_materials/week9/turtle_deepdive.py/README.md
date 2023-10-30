# Practice 1

Below is an approximation of an assignment you might be given related to using `turtle`.

Also included (but hidden in a folder, `example_solutions` for "spoilers" reasons) are three example solutions.

If you already feel very comfortable with turtle from readings, you can just glance through the examples.

However, you are recommended to start by trying this yourself in a blank .py file.

Then, after you've tried for 5-10 minutes, scroll down in this file to receive incremental hints.

After you're done, take a look at the examples.

The assignment prompt:

Using Python’s turtle module, create a script that generates a unique piece of abstract art. 
Utilize the random module to ensure that each run of your script produces a different artwork.
Try to use various turtle methods such as forward(), right(), left(), penup(), pendown(), color(), and speed(). 
You may define additional functions to organize your code as necessary. 
Be creative and have fun (hopefully)!


Suggested approaches:

- try drawing random lines
- try drawing random circles and lines
- try drawing random squares
- advanced: try using a mathematical function like sin `import math -> math.sin()`


Suggested coding tips:
- to start getting some practice with functions, try putting your main body of code in a function called `main` and then call `main()` at the bottom of the file. See also `starterkit.py` if you feel totally stuck.


SCROLL DOWN AFTER 5-10 MINUTES OF TINKERING
=
=
=
=
=
=
=
=
=
=
=
=
=
=

If you're stuck, you might want to try creating a function to create random lines. For instance:


```
def draw_random_lines(num_lines):
    for _ in range(num_lines):
        # pick a random color
        t.color(random.random(), random.random(), random.random())
        t.penup()
        t.goto(random.randint(-200, 200), random.randint(-200, 200))
        t.pendown()
        t.setheading(random.randint(0, 360))
        t.forward(random.randint(50, 200))
```

then, you can call this function under main(), e.g. `draw_random_lines(5)` to draw 5 lines.

From there, you can start to think about how you might draw circles or squares.








