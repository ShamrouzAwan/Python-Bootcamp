# Day 3, Section 2: Modulo Operator and Checking Odd or Even Numbers

# The modulo operator (%) gives the remainder of a division.
print(6 % 2)  # Outputs: 0 (6 is divisible by 2)
print(6 % 5)  # Outputs: 1 (6 divided by 5 has a remainder of 1)
print(6 % 4)  # Outputs: 2 (6 divided by 4 has a remainder of 2)

# PAUSE 1: What is 10 % 3?
# This will output the remainder of the division of 10 by 3.
print(10 % 3)  # Outputs: 1 (10 divided by 3 has a remainder of 1)

# PAUSE 2: Check Odd or Even
# Use the modulo operator and conditional checks to determine if a number is odd or even.

# Get user input and convert it to an integer
number = int(input("Enter a number: "))

# Check if the number is odd or even
if number % 2 == 0:
    print("Even")  # If the remainder when divided by 2 is 0, it's even
else:
    print("Odd")   # If the remainder is not 0, it's odd
