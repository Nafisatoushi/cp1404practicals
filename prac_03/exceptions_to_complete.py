"""
CP1404 - Prac - 03
Filling the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        break   # add a break statement
    except ValueError:    # specifying the exception type
        print("Please enter a valid integer.")
print("Valid result is:", result)
