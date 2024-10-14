# Day 4, Section 4: IndexError, Length of List, and Nested Lists

# Length of a List
fruits = ["Cherry", "Apple", "Pear"]
print("Number of fruits:", len(fruits))  # Output the length of the fruits list

# Example of IndexError
try:
    print(fruits[3])  # This will raise an IndexError
except IndexError:
    print("IndexError: The index is out of range for the fruits list.")

# Nested Lists
veg = ["Cucumber", "Kale", "Spinach"]
fruits_and_veg = [fruits, veg]
print("Fruits and Vegetables List:")
print(fruits_and_veg)  # Output the nested list

# Printing in a 2D format
print("Fruits:")
for fruit in fruits:
    print(fruit)

print("Vegetables:")
for vegetable in veg:
    print(vegetable)

# States of America List
states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", 
    "Virginia", "New York", "North Carolina", "Rhode Island", 
    "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", 
    "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", 
    "Missouri", "Arkansas", "Michigan", "Florida", "Texas", 
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", 
    "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", 
    "North Dakota", "South Dakota", "Montana", "Washington", 
    "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", 
    "Arizona", "Alaska", "Hawaii"
]

print("States of America:")
print(states_of_america)  # Output the states list
