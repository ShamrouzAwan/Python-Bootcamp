# Day 3, Section 5: Automatic Pizza Order Program

# Welcome message and user input for pizza order preferences
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Initialize the bill variable
bill = 0

# Calculate the base price based on pizza size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have chosen an invalid size.")

# Calculate additional costs based on pepperoni choice
if pepperoni == "Y":
    if size == "S":
        bill += 2  # Small pizza pepperoni
    else:
        bill += 3  # Medium or large pizza pepperoni

# Calculate final amount based on extra cheese choice
if extra_cheese == "Y":
    bill += 1  # Extra cheese cost

# Output the final bill
print(f"Your final bill is: ${bill}.")
