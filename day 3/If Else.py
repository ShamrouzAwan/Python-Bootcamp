# Day 3, Section 1: Condition Check in Python

# Using if/else to check a condition:
# The "if" keyword checks whether a condition is true.
# If it's true, the code inside the if block will execute.
# If the condition is false, the "else" block will execute.

if 5 > 2:
    print("Yes, 5 is greater than 2!")  # This line runs because the condition is true
else:
    print("No, 5 is not greater than 2.")  # This line will not run

# Another example with a false condition:
if False:
    print("This won't print because the condition is false.")
else:
    print("This will print because the condition is false.")

# Python Indentation:
# Indentation is important in Python to define blocks of code.
# Child lines (inside if/else) must be indented under parent lines (if/else conditions).

if 10 == 10:  # Parent line
    print("This will print because 10 is equal to 10.")  # Child line

# Comparator Operators:
# You can compare values using the following operators:
# >  : Greater than
# <  : Less than
# >= : Greater than or equal to
# <= : Less than or equal to
# == : Equal to
# != : Not equal to

a = 10
b = 5

print(a > b)   # True because 10 is greater than 5
print(a < b)   # False because 10 is not less than 5
print(a >= 10) # True because 10 is greater than or equal to 10
print(a == b)  # False because 10 is not equal to 5
print(a != b)  # True because 10 is not equal to 5
