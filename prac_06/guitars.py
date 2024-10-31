from guitar import Guitar

def get_guitar_details():
    name = input("Name: ")
    if not name:
        return None
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    return Guitar(name, year, cost)

def display_guitars(guitars):
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

def main():
    print("My guitars!")
    guitars = []

    # Test data for guitars
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    guitar = get_guitar_details()
    while guitar is not None:
        guitars.append(guitar)
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:.2f} added.\n")
        guitar = get_guitar_details()

    display_guitars(guitars)

main()
