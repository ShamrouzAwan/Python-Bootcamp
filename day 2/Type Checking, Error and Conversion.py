# Day 2, Section 2: TypeError, Type Checking, and Type Conversion in Python

# TypeError example:
# Trying to use len() on an integer will raise a TypeError
# Uncomment the line below to see the error:
# print(len(12345))

# PAUSE 1: Fix the len() function so it has no more warnings or errors.
# Solution: Convert the number to a string to use len()
print(len(str(12345)))  # Now it works because we converted the number to a string

# Type Checking
# You can check the data type of any value or variable using the type() function.

# PAUSE 2: Write out 4 type checks to print all 4 data types
print(type("abc"))  # Outputs: <class 'str'>
print(type(123))    # Outputs: <class 'int'>
print(type(3.14))   # Outputs: <class 'float'>
print(type(True))   # Outputs: <class 'bool'>

# Type Conversion
# You can convert data into different data types using special functions.

# Example:
print(float(123))   # Converts integer to float
print(int(3.14))    # Converts float to integer
print(str(123))     # Converts integer to string

# PAUSE 3: Fix the following line of code to run without errors:
# Original: print("Number of letters in your name: " + len(input("Enter your name")))
# Solution: Convert the length (which is an integer) to a string before concatenation.
print("Number of letters in your name: " + str(len(input("Enter your name: "))))
