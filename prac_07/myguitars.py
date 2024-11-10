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


def get_new_guitar():
    """Get details of a new guitar from the user."""
    name = input("Enter the name of the guitar: ")
    year = int(input("Enter the year the guitar was made: "))
    cost = float(input("Enter the cost of the guitar: $"))
    return Guitar(name, year, cost)

def save_guitars_to_file(guitars, file_name):
    """Save guitars to a file."""
    with open(file_name, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

def main():
    guitars = load_guitars_from_file('guitars.csv')
    guitars.sort()

    # Display existing guitars
    print("Existing Guitars:")
    for guitar in guitars:
        print(guitar)


main()