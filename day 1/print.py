# Day 1: Learning Simple Printing in Python

# Printing "Hello world" with a newline character (\n)
print("Hello world\nHello world")

# Updating the code to add an exclamation mark
print("Hello world!")

# Asking for user input and checking the length of the input
user_input = input("Enter something: ")
print(f"Length of your input: {len(user_input)}")

# Variable naming rules
# - Variable names should start with a letter or an underscore (_)
# - Cannot start with a number
# - Variable names are case-sensitive
# - Should not use Python keywords like 'print', 'input', etc.

# Creating a greeting for the program
print("Welcome to the Band Name Generator!")

# Asking the user for the city they grew up in and storing it in a variable
city = input("What's the name of the city you grew up in?\n")

# Asking the user for the name of their pet and storing it in a variable
pet = input("What's the name of your pet?\n")

# Combining the city and pet name to suggest a band name
band_name = city + " " + pet
print("Your band name could be: " + band_name)
