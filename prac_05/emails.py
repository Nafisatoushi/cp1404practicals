def main():
    user_data = {}
    email = input("Email: ")

    while email:
        # Check for a valid email
        if '@' not in email or '.' not in email:
            print("Invalid email")
        else:
            name = extract_name(email)
            is_correct = input(f"Is your name {name}? (Y/n) ").strip().lower()

            if is_correct == '' or is_correct == 'y':
                user_data[email] = name
            else:
                user_name = input("Name: ")
                user_data[email] = user_name

        email = input("Email: ")

    # Print user data
    for email, name in user_data.items():
        print(f"{name} ({email})")

