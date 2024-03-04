"""CP-1404 - Prac_03
asking for and validating a person's password"""
MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print(f"\tand 1 or more special characters: {SPECIAL_CHARACTERS}")

    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")

    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # Check if the length is within the specified range
    if not (MIN_LENGTH <= len(password) <= MAX_LENGTH):
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    # Count each kind of character
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif SPECIAL_CHARS_REQUIRED and char in SPECIAL_CHARACTERS:
            count_special += 1

    # Check if at least one of each kind of character is present
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    # Check if special characters are required and at least one is present
    if SPECIAL_CHARS_REQUIRED and count_special == 0:
        return False

    # If all checks pass, the password is valid
    return True


main()
