# Day 2, Section 5: Tip Calculator Project

# Tip Calculator Example:
# If the bill is $150, split between 5 people with a 12% tip,
# each person should pay (150 / 5) * 1.12 = 33.60.

# Project solution:
print("Welcome to the tip calculator!")

# Ask the user for the total bill amount and convert it to a float
bill = float(input("What was the total bill? $"))

# Ask the user for the tip percentage and convert it to an integer
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Ask the user how many people are splitting the bill and convert it to an integer
people = int(input("How many people to split the bill? "))

# Calculate the tip as a percentage
tip_as_percent = tip / 100

# Calculate the total tip amount
total_tip_amount = bill * tip_as_percent

# Calculate the total bill including the tip
total_bill = bill + total_tip_amount

# Calculate how much each person should pay
bill_per_person = total_bill / people

# Round the result to 2 decimal places
final_amount = round(bill_per_person, 2)

# Print the final amount each person should pay
print(f"Each person should pay: ${final_amount}")
