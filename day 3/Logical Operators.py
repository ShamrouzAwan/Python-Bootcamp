# Day 3, Section 6: Combining Conditions Using Logical Operators

# Logical operators:
# - A and B: Both conditions must be true.
# - C or D: At least one condition must be true.
# - not E: The condition must be false.

# Example: Determine if a person can ride for free based on their age.
age = int(input("Enter your age: "))

# Check if the age is less than 18, over 65, or between 45 and 55 (inclusive).
if age < 18 or age > 65 or (age >= 45 and age <= 55):
    print("You can ride for free!")
else:
    print("You need to pay for the ride.")

# Note: The condition checking for ages 45 to 55 uses the 'and' operator to combine conditions.
