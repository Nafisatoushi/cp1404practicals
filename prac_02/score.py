"""
CP1404 - prac_01
Broken program to determine score status
"""

import random

def main():
    """Main function to ask for the user's score and generate a random score."""
    user_score = float(input("Enter your score: "))
    user_result = determine_score_status(user_score)
    print(f"Your result: {user_result}")

    random_score = random.randint(0, 100)
    random_result = determine_score_status(random_score)
    print(f"Random score ({random_score}): {random_result}")

def determine_score_status(score):
    """Determine the score status based on the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
