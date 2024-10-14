# Day 4, Section 1: Random Module

# Introduction to Pseudorandom Number Generators
# Computers generate pseudorandom numbers because they are built with circuits and switches. 
# These numbers are crucial for applications like gaming, where predictability is boring.

# Importing the random module
import random

# Generating Random Whole Numbers Within a Range
rand_num = random.randint(1, 10)  # Produces a random whole number between 1 and 10 (inclusive)
print(f"Random whole number between 1 and 10: {rand_num}")

# Generating Random Floats
rand_num_0_to_1 = random.random()  # Generates a random number between 0 (not inclusive) and 1 (inclusive)
print(f"Random float between 0 and 1: {rand_num_0_to_1}")

# Expanding the range of random numbers generated
expanded_random = random.random() * 5  # Generates a random number between 0 and 5
print(f"Random float between 0 and 5: {expanded_random}")

# Using the uniform() function to generate random floating point numbers
random_float = random.uniform(1, 10)  # Generates a random floating point number between 1 and 10
print(f"Random float between 1 and 10: {random_float}")
