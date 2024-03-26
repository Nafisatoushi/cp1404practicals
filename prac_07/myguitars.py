from guitar import Guitar
import csv

def load_guitars(file_name):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            name, year, cost = line
            year = int(year)
            cost = float(cost)
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    """Display details of guitars in a list."""
    print("My Guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

def sort_guitars_by_year(guitars):
    """Sort guitars by year."""
    guitars.sort()

def main():
    # Load guitars from the CSV file
    guitars = load_guitars("guitars.csv")

    # Display unsorted guitars
    display_guitars(guitars)

    # Sort guitars by year and display sorted list
    sort_guitars_by_year(guitars)
    print("\nSorted Guitars:")
    display_guitars(guitars)

main()
