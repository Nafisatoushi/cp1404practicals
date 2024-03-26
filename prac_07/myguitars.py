from guitar import Guitar
import csv

def load_guitars_from_file(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def write_guitars_to_file(filename, guitars):
    """Write guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

def add_new_guitar(guitars):
    """Add a new guitar to the list."""
    name = input("Enter the name of the guitar: ")
    year = int(input("Enter the year of manufacture: "))
    cost = float(input("Enter the cost of the guitar: "))
    guitars.append(Guitar(name, year, cost))

def main():
    # Load existing guitars from the file
    filename = 'guitars.csv'
    guitars = load_guitars_from_file(filename)

    # Display existing guitars
    print("Existing guitars:")
    for guitar in guitars:
        print(guitar)

    # Add a new guitar
    add_new_guitar(guitars)

    # Write all guitars to the file
    write_guitars_to_file(filename, guitars)
    print("New guitar added and saved to file.")

main()
