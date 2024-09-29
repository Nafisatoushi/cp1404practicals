def get_password(min_length):
    password = input("Enter a password: ")
    if len(password) >= min_length:
        return password
    else:
        print(f"Password must be at least {min_length} characters long. Try again.")

def print_password_asterisks(password):
    print("*" * len(password))

def main():
    min_password_length = 8  # You can set the minimum length as needed
    user_password = get_password(min_password_length)
    print("Password Accepted! Here is the visual representation:")
    print_password_asterisks(user_password)

main()