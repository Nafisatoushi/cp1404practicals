"""Password Check Program"""

def main():
    """Main function to execute the program."""
    user_password = get_password()
    print("Password Accepted! Here is the visual representation:")
    print_password_asterisks(user_password)


def get_password():
    global get_password

    def get_password():
        """Function to get a password from the user."""
        password = input("Enter a password: ")
        while len(password) < 8:
            print("Password must be at least 8 characters long. Try again.")
            password = input("Enter a password: ")
        return password


get_password()

def print_password_asterisks(password):
    """Function to print asterisks based on the length of the password."""
    print("*" * len(password))

main()
