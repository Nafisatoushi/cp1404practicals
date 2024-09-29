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