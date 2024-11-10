class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """__it__ method for sorting by year"""
        """Compare Guitars by year."""
        return self.year < other.year



    def get_age(self):
        """Return the age of the guitar in years."""
        current_year = 2022  # Assuming the current year is 2022
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50