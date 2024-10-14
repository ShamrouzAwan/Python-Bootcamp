# Day 4, Section 2: Lists

# Creating a simple collection of ordered items
fruits = ["Cherry", "Apple", "Pear"]
print(f"Initial fruits list: {fruits}")

states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
    "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont",
    "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
    "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
    "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
    "North Dakota", "South Dakota", "Montana", "Washington", "Idaho",
    "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

# Accessing Items in Lists
first_state = states_of_america[0]  # This will give you "Delaware"
print(f"The first state in the list is: {first_state}")

# Negative Indices
last_fruit = fruits[-1]  # This will be "Pear"
print(f"The last fruit in the list is: {last_fruit}")

# Modifying Items
fruits[0] = "Orange"  # Changing "Cherry" to "Orange"
print(f"Fruits after modification: {fruits}")

# Adding Items
fruits.append("Orange")  # Adding "Orange" to the end of the list
print(f"Fruits after appending: {fruits}")

# Reference to Python Lists Documentation
# You can find more about lists and their functions at:
# https://docs.python.org/3/tutorial/datastructures.html
