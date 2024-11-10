class Project:
    """class for project management"""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare projects by priority for sorting."""
        return self.priority < other.priority

    def is_complete(self):
        """Check if the project is complete."""
        return self.completion_percentage == 100

    def to_string(self):
        """utility/helper method"""
        """Convert a Project object to a string for saving."""
        return (f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t"
                f"{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}")
