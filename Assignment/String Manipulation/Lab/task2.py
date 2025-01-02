# Demonstrating various string methods in Python

# Example string
text = "   Hello, World!   "

# Strip leading and trailing whitespace
stripped_text = text.strip()
print(f"Stripped text: '{stripped_text}'")

# Convert to uppercase
upper_text = stripped_text.upper()
print(f"Uppercase text: '{upper_text}'")

# Convert to lowercase
lower_text = stripped_text.lower()
print(f"Lowercase text: '{lower_text}'")

# Capitalize the first letter
capitalized_text = stripped_text.capitalize()
print(f"Capitalized text: '{capitalized_text}'")

# Title case (first letter of each word capitalized)
title_text = stripped_text.title()
print(f"Title case text: '{title_text}'")

# Replace a substring
replaced_text = stripped_text.replace("World", "Python")
print(f"Replaced text: '{replaced_text}'")

# Find the index of a substring
index = stripped_text.find("World")
print(f"Index of 'World': {index}")

# Check if the string starts with a substring
starts_with_hello = stripped_text.startswith("Hello")
print(f"Starts with 'Hello': {starts_with_hello}")

# Check if the string ends with a substring
ends_with_world = stripped_text.endswith("World!")
print(f"Ends with 'World!': {ends_with_world}")

# Split the string into a list of words
split_text = stripped_text.split()
print(f"Split text: {split_text}")

# Join a list of strings into a single string
joined_text = ' '.join(split_text)
print(f"Joined text: '{joined_text}'")

# Count occurrences of a substring
count_l = stripped_text.count('l')
print(f"Occurrences of 'l': {count_l}")

