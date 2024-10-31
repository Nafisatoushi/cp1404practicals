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