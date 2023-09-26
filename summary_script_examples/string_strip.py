# Basic usage of .strip()
basic_string = "   Hello, World!   "
print("Original:", repr(basic_string))
print("Stripped:", repr(basic_string.strip()))
print("----------------------")

# 1. Removing spaces:
# By default, .strip() removes leading and trailing whitespaces.
spaces_string = "   Spaces around   "
print("Original:", repr(spaces_string))
print("Stripped:", repr(spaces_string.strip()))
print("----------------------")

# 2. Removing specific characters:
# You can specify characters to be removed. 
chars_string = "zzzyHello, World!yzzz"
print("Original:", repr(chars_string))
print("Stripped:", repr(chars_string.strip('z')))
print("----------------------")

# 3. Removing multiple types of characters:
# You can specify multiple characters to be removed.
multi_chars_string = "xxxyHello, World!yzzz"
print("Original:", repr(multi_chars_string))
print("Stripped:", repr(multi_chars_string.strip('xyz')))
# Notice how all the leading 'x', 'y', and 'z' characters and the trailing 'y' and 'z' characters were removed.
print("----------------------")

# 4. Common confusion: Order doesn't matter in the argument.
confusing_string = "yxzHello, World!zyx"
print("Original:", repr(confusing_string))
print("Stripped with 'xyz':", repr(confusing_string.strip('xyz')))
print("Stripped with 'zyx':", repr(confusing_string.strip('zyx')))
# Both are equivalent. The order of characters in the argument doesn't dictate the order of removal.
print("----------------------")

# 5. Not removing middle characters:
middle_string = "abcHello, World!cbaHello, World!abc"
print("Original:", repr(middle_string))
print("Stripped:", repr(middle_string.strip('abc')))
# Note that .strip() only removes characters from the start and end. 'abc' in the middle remains unaffected.
print("----------------------")

# 6. Using .lstrip() and .rstrip():
# For stripping characters only from the left or right side.
side_string = "xxHello, World!yy"
print("Original:", repr(side_string))
print("Left Stripped:", repr(side_string.lstrip('x')))
print("Right Stripped:", repr(side_string.rstrip('y')))
print("----------------------")
