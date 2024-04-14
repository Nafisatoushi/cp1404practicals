class Band:
    """A Band class that holds a collection of musicians."""

    def __init__(self, name):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Show which musicians are playing and their instruments."""
        output = []
        for musician in self.musicians:
            output.append(musician.play())
        return "\n".join(output)

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"