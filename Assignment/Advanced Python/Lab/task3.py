# Define a function to check if a number is odd
def is_odd(number):
    return number % 2 != 0

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() to filter out even numbers (keep only odd numbers)
odd_numbers = filter(is_odd, numbers)

# Convert the filter object to a list and print the result
odd_numbers_list = list(odd_numbers)
print("The list of odd numbers is:", odd_numbers_list)
