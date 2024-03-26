# Importing necessary classes and modules
from guitar import Guitar


def load_guitars_from_file(file_name):
    """Load guitars from a file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                name = parts[0]
                year = int(parts[1])
                cost = float(parts[2])
                guitar = Guitar(name, year, cost)
                guitars.append(guitar)
    except FileNotFoundError:
        print("File not found. Creating a new file...")
    return guitars


def save_guitars_to_file(guitars, file_name):
    """Save guitars to a file."""
    with open(file_name, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def get_new_guitar():
    """Get details of a new guitar from the user."""
    name = input("Enter the name of the guitar: ")
    year = int(input("Enter the year the guitar was made: "))
    cost = float(input("Enter the cost of the guitar: $"))
    return Guitar(name, year, cost)


def main():
    guitars = load_guitars_from_file('guitars.csv')

    # Display existing guitars
    print("Existing Guitars:")
    for guitar in guitars:
        print(guitar)

    # Get details of new guitars from the user
    num_new_guitars = int(input("How many new guitars do you want to add? "))
    for i in range(num_new_guitars):
        print(f"\nEntering details for Guitar #{i + 1}:")
        new_guitar = get_new_guitar()
        guitars.append(new_guitar)

    # Save guitars to file
    save_guitars_to_file(guitars, 'guitars.csv')
    print("\nNew guitars saved to file.")

    # Display all guitars after adding new ones
    print("\nAll Guitars:")
    for guitar in guitars:
        print(guitar)


main()
