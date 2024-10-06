"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
# Answer 1:  ValueError will occur if the user enters a non-integer for numerator or denominator.

# Answer 2:ZeroDivisionError will occur if the user enters 0 for the denominator.

# Answer 3:Yes, we can change the code to check if the denominator is zero before performing the division.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")