# Day 2, Section 4: Flooring, Rounding, Assignment Operators, and f-Strings in Python

# Flooring a Number
# You can floor a number (remove all decimal places) using the int() function.
print(int(3.738492))  # Outputs: 3

# Rounding a Number
# Use round() to round to the nearest whole number.
print(round(3.738492))  # Outputs: 4
print(round(3.14159))   # Outputs: 3

# You can also round to a specific number of decimal places by adding a second argument.
print(round(3.14159, 2))  # Outputs: 3.14

# Assignment Operators
# Assignment operators allow you to perform operations and update the variable in one step.
x = 10
x += 5  # Adds 5 to x
print(x)  # Outputs: 15

y = 20
y *= 2  # Multiplies y by 2
print(y)  # Outputs: 40

# -= and /= can be used similarly for subtraction and division:
z = 30
z -= 10  # Subtracts 10 from z
print(z)  # Outputs: 20

a = 50
a /= 5  # Divides a by 5
print(a)  # Outputs: 10.0

# f-Strings
# f-strings are used to format strings and include variables directly within the string.
age = 12
print(f"I am {age} years old")  # Outputs: I am 12 years old.

# You can also include expressions in f-strings:
height = 5.9
print(f"My height is {height} feet")  # Outputs: My height is 5.9 feet
