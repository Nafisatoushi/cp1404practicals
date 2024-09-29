"""
CP1404 - prac_02
Score Menu Program
"""

def main():
    """Main function to execute the score menu."""
    score = get_valid_score()

    choice = display_menu()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option. Please try again.")

        choice = display_menu()

    print("Farewell! Thanks for using the Score Menu.")

def get_valid_score():
    """Get a valid score from the user."""
    score = float(input("Enter a valid score (0-100): "))
    while not (0 <= score <= 100):
        print("Invalid score. Please enter a score between 0 and 100.")
        score = float(input("Enter a valid score (0-100): "))
    return score