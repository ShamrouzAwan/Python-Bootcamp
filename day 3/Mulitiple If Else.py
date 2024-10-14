# Day 3, Section 4: Understanding If/Elif/Else, Nested If Statements, and Multiple If Statements

# If/elif/else structure:
# Only one of the conditions can be true at a time.
if <condition 1 is true>:
    <do A>
elif <condition 2 is true>:
    <do B>
else:
    <do C>

# Example:
temperature = 30
if temperature > 25:
    print("It's hot outside.")
elif temperature > 15:
    print("It's a pleasant day.")
else:
    print("It's cold outside.")

# Nested if statements:
# Allows for multiple layers of conditions, but only checks the next condition if the previous one is true.
if <condition 1 is true>:
    <do A>
    if <condition 2 is true>:
        <do B>
        if <condition 3 is true>:
            <do C>

# Example:
score = 85
if score >= 90:
    print("Excellent!")
    if score >= 95:
        print("You're a top performer!")
elif score >= 80:
    print("Well done!")
    if score >= 85:
        print("You did great!")

# Multiple if statements:
# Each condition is independent; all conditions are checked regardless of the others.
if <condition 1 is true>:
    <do A>
if <condition 2 is true>:
    <do B>
if <condition 3 is true>:
    <do C>

# Example:
if temperature > 20:
    print("It's warm.")
if temperature < 15:
    print("It's cold.")
if score < 50:
    print("You need to improve.")

# Summary:
# - In the if/elif/else block, only one of A, B, or C can execute.
# - In nested if statements, A, B, and C can all execute, but must be in a true hierarchy.
# - In multiple if statements, A, B, and C can all execute independently of one another.
