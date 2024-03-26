import csv
from project import Project

def load_projects(filename="projects.txt"):
    """Load projects from the specified file."""
    projects = []
    with open(filename, "r") as file:
        reader = csv.reader(file, delimiter="\t")
        next(reader)  # Skip header
        for row in reader:
            name, start_date, priority, cost_estimate, completion_percentage = row
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
    return projects

def main():
    """Main function to manage projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    print(f"Loaded {len(projects)} projects from projects.txt")

main()