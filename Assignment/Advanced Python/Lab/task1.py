# Define a function to square a number
def square(number):
    return number ** 2

# List of numbers to be squared
numbers = [1, 2, 3, 4, 5]

# Use map() to apply the square function to each number in the list
squared_numbers = map(square, numbers)

# Convert the map object to a list and print the result
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)
