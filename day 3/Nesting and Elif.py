# Day 3, Section 3: Nesting If/Else Statements

# You can nest if/else statements within other if/else statements.
# This allows for more complex conditional checks.

# Example: Checking scores in maths and English
maths_score = 92
english_score = 85

if maths_score >= 90:
    if english_score >= 90:
        print("You're good at everything")  # Executes if both conditions are true
    else:
        print("You're good at maths")  # Executes if maths_score is >= 90 and english_score is < 90

# Check separately for English score
if english_score >= 90:
    print("You're good at English")  # Executes if english_score is >= 90

# Note: If statements don't have to have a paired else statement.
# You can simply check multiple conditions without needing an else clause.
