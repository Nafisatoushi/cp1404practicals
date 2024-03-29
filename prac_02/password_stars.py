"""
CP1404/CP5632 - Practical - Suggested Solution
Get a password with minimum length and display asterisks
"""

MIN_LENGTH = 8

def get_and_display_password():
    """Get a password of valid size and print asterisks."""
    password = input(f"Enter password of at least {MIN_LENGTH} characters: ")
    while len(password) < MIN_LENGTH:
        password = input(f"Enter password of at least {MIN_LENGTH} characters: ")

    print('*' * len(password))


# version_2()


def main():
    """Get and print password using functions."""
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password, ensuring it meets the minimum_length requirement."""
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password


def print_asterisks(sequence):
    """Print as many asterisks as there are characters in the passed-in sequence."""
    print('*' * len(sequence))


main()
