# Day 2, Section 3: Basic Operators and PEMDAS in Python

# Basic Mathematical Operators:
# + : Addition
# - : Subtraction
# * : Multiplication
# / : Division (returns a float)
# // : Floor Division (returns an integer)
# ** : Exponentiation (raises to the power)

# PEMDAS:
# Python follows the standard order of operations:
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

# PAUSE 1: What is the output of this code?
# According to PEMDAS, the output will be calculated as:
# 3 * 3 = 9
# 3 / 3 = 1
# 9 + 1 - 3 = 7
print(3 * 3 + 3 / 3 - 3)  # Outputs: 7.0

# PAUSE 2: Change the code so it outputs 3.
# We can modify the code by using parentheses to change the order of operations.
# Example:
print(3 * (3 + 3) / 3 - 3)  # Outputs: 3.0
