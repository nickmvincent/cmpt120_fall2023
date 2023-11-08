import copy

# Defining a variable as an alias
original_list_of_lists = [[1, 2], [3, 4]]
alias_list_of_lists = original_list_of_lists  # Both point to the same list of lists

# Defining a variable as a clone (shallow copy)
clone_list_of_lists = original_list_of_lists[:]  # Creates a shallow copy of the list of lists
clone_list_of_lists_via_constructor = list(original_list_of_lists)  # Another way to create a shallow copy

# Defining a variable as a deepcopy
deepcopy_list_of_lists = copy.deepcopy(original_list_of_lists)  # Creates a deep copy of the list of lists

# Function that modifies a list of lists passed by reference
def modify_list_of_lists(input_list_of_lists):
    input_list_of_lists[0].append('modified')  # This will modify the first inner list
    input_list_of_lists.append([5, 6])  # This will add a new inner list to the list of lists
    return input_list_of_lists

# Passing a list of lists by reference
modify_list_of_lists(original_list_of_lists)

# Output the results
print("Original List of Lists (modified by reference):", original_list_of_lists)
print("Alias List of Lists (also modified):", alias_list_of_lists)
print("Clone List of Lists (inner list modified):", clone_list_of_lists)
print("Clone List of Lists via Constructor (inner list modified):", clone_list_of_lists_via_constructor)
print("Deepcopy List of Lists (unmodified):", deepcopy_list_of_lists)
