# Get user's name
name = input("Enter name: ")

# Display menu function
def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

# Display initial menu
display_menu()

# Get initial choice
choice = input(">>> ").upper()

# Main loop
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    # Display menu again
    display_menu()

    # Get next choice
    choice = input(">>> ").upper()

# Final message
print("Finished.")
