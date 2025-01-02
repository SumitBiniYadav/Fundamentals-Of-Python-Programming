from functools import reduce

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Use reduce() to apply the multiply function to the list of numbers
product = reduce(multiply, numbers)

