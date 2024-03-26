# Importing necessary classes and modules
from guitar import Guitar
import csv

# Function to load guitars from the CSV file
def load_guitars_from_file(filename):
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

# Function to display guitars
def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)

# Function to sort guitars by year
def sort_guitars_by_year(guitars):
    guitars.sort()

# Main function
def main():
    # Loading guitars from file
    guitars = load_guitars_from_file('guitars.csv')

    # Displaying unsorted guitars
    print("Unsorted Guitars:")
    display_guitars(guitars)

    # Sorting guitars by year
    sort_guitars_by_year(guitars)

    # Displaying sorted guitars
    print("\nSorted Guitars by Year (Oldest to Newest):")
    display_guitars(guitars)

# Executing main function
main()
