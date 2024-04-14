class Band:
    """A Band class that holds a collection of musicians."""

    def __init__(self, name):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []