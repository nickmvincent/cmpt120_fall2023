#%%
import copy

#%%
a = [1,2,3]

b = a

c = a[:]

#%%
a = [[1,2],[3,4]]
b = a
c = a[:]

a[0][0] = 100

print(a)
print(b)
print(c)

#%%
a = [[1,2],[3,4]]
b = a
c = copy.deepcopy(a)

a[0][0] = 100

print(a)
print(b)
print(c)

#%%
tensor = [
    [
        [1,2],
        [3,4],
    ],
    [
        [5,6],
        [7,8],
    ]
]
matrix = tensor[0]
first_row = matrix[0]
print(first_row)
first_row[0] = 100
print(matrix)
print(tensor)

last_row = tensor[-1][-1]
last_row = [1000,1000]
print(tensor)

#%%

# COLOR CHANGE SNIPPET 1

# Turn red to blue and white to black
# edit the original image
X = [
        [[1,0,0], [0,1,0]],
        [[0,0,1], [1,0,0]],
        [[1,1,1], [1,1,1]]
    ]
    
for row_index in range(len(X)):
    for col_index in range(len(X[0])):
        X[row_index][col_index]
        if X[row_index][col_index] == [1,0,0]:
            X[row_index][col_index] = [0,0,1]
            print("Changed red to blue")
        if X[row_index][col_index] == [1,1,1]:
            X[row_index][col_index] = [0,0,0]
            print("Changed white to black")

for row in X:
    print(row)

#%%

# COLOR CHANGE SNIPPET 2

# Let's try to avoid repeating ourselves
# X[row_index][col_index] appears a lot
# create a variable for it?
X = [
        [[1,0,0], [0,1,0]],
        [[0,0,1], [1,0,0]],
        [[1,1,1], [1,1,1]]
    ]
    
for row_index in range(len(X)):
    for col_index in range(len(X[0])):
        current_pixel = X[row_index][col_index]
        if current_pixel == [1,0,0]:
            X[row_index][col_index] = [0,0,1]
            print("Changed red to blue")
        if current_pixel == [1,1,1]:
            X[row_index][col_index] = [0,0,0]
            print("Changed white to black")

for row in X:
    print(row)


#%%

# COLOR CHANGE SNIPPET 3

# What if we replace all instances
# of X[row_index][col_index]
# with current_pixel
# when we assign, it doesn't edit X!
# Something goes wrong!
X = [
        [[1,0,0], [0,1,0]],
        [[0,0,1], [1,0,0]],
        [[1,1,1], [1,1,1]]
    ]
    
for row_index in range(len(X)):
    for col_index in range(len(X[0])):
        current_pixel = X[row_index][col_index]
        if current_pixel == [1,0,0]:
            current_pixel = [0,0,1]
            print("Changed red to blue")
        if current_pixel == [1,1,1]:
            current_pixel = [0,0,0]
            print("Changed white to black")

for row in X:
    print(row)


#%%
# COLOR CHANGE SNIPPET 4

# this doesn't work! How come?
X = [
        [[1,0,0], [0,1,0]],
        [[0,0,1], [1,0,0]],
        [[1,1,1], [1,1,1]]
    ]
    
for row_index in range(len(X)):
    cur_row = X[row_index]
    for col_index in range(len(X[0])):
        current_pixel = cur_row[col_index]
        if current_pixel == [1,0,0]:
            current_pixel = [0,0,1]
            print("Changed red to blue")
        if current_pixel == [1,1,1]:
            current_pixel = [0,0,0]
            print("Changed white to black")

for row in X:
    print(row)
#%%
# COLOR CHANGE SNIPPET 5

# If we change the color values one at a time,
# it works...
X = [
        [[1,0,0], [0,1,0]],
        [[0,0,1], [1,0,0]],
        [[1,1,1], [1,1,1]]
    ]
    
for row_index in range(len(X)):
    cur_row = X[row_index]
    for col_index in range(len(X[0])):
        current_pixel = cur_row[col_index]
        if current_pixel == [1,0,0]:
            current_pixel[0] = 0
            current_pixel[1] = 0
            current_pixel[2] = 1
            print("Changed red to blue")
        if current_pixel == [1,1,1]:
            current_pixel[0] = 0
            current_pixel[1] = 0
            current_pixel[2] = 0
            print("Changed white to black")

for row in X:
    print(row)

#%%

# using deep copy so we keep our
# original X
X = [
        [[1,0,0], [0,1,0]],
        [[0,0,1], [1,0,0]],
        [[1,1,1], [1,1,1]]
    ]
X_for_editing = copy.deepcopy(X)
    
for row_index in range(len(X_for_editing )):
    for col_index in range(len(X_for_editing [0])):
        current_pixel = X_for_editing[row_index][col_index]
        if current_pixel == [1,0,0]:
            X_for_editing[row_index][col_index] = [0,0,1]
            print("Changed red to blue")
        if current_pixel == [1,1,1]:
            X_for_editing[row_index][col_index] = [0,0,0]
            print("Changed white to black")

for row in X_for_editing:
    print(row)


# %%

# manually construct a new matrix
X = [
        [[1,0,0], [0,1,0]],
        [[0,0,1], [1,0,0]],
        [[1,1,1], [1,1,1]]
    ]
new_X = []
    
for row_index in range(len(X)):
    new_row = []
    for col_index in range(len(X[0])):
        current_pixel = X[row_index][col_index]
        if current_pixel == [1,0,0]:
            new_row.append([0,0,1])
        elif current_pixel == [1,1,1]:
            new_row.append([0,0,0])
        else:
            new_row.append(current_pixel)
    new_X.append(new_row)

for row in new_X:
    print(row)

# %%
