# Hello, and welcome to our interactive code

#%%
import turtle

#%%
t = turtle.Turtle()

#%%
t.forward(100)
# %%
t.stamp()
# %%
t.forward(100)
# %%
t.right(90)
# %%
t.forward(100)

#%%
t.left(180)
t.forward(200)

#%%
t.penup()
t.left(90)
t.forward(200)

t.pendown()
t.forward(100)

t.goto(0,0)
t.color("blue")
t.forward(100)