# Demonstrating string slicing in Python

# Example string
text = "Hello, World!"

# Slice from the start to the fifth character (excluding index 5)
slice1 = text[:5]
print(f"Slice from start to index 5: '{slice1}'")

# Slice from the seventh character to the end
slice2 = text[7:]
print(f"Slice from index 7 to end: '{slice2}'")

# Slice from the third to the eighth character (excluding index 8)
slice3 = text[2:8]
print(f"Slice from index 2 to 8: '{slice3}'")

# Slice the entire string
slice4 = text[:]
print(f"Entire string: '{slice4}'")

# Slice with a step
slice5 = text[::2]
print(f"Every second character: '{slice5}'")

# Reverse the string using slicing
slice6 = text[::-1]
print(f"Reversed string: '{slice6}'")

# Negative indexing: slice from the end
slice7 = text[-6:]
print(f"Last 6 characters: '{slice7}'")

