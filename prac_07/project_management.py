"""Estimate time: 40Mins
Actual time:"""
import datetime
from project import Project

def load_projects_from_file(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]  # Skip header line
        for line in lines:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            projects.append(Project(name, datetime.datetime.strptime(start_date, "%d/%m/%Y").date(), int(priority), float(cost_estimate), int(completion_percentage)))
    return projects

def save_projects_to_file(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")  # Header
        for project in projects:
            file.write(project.to_string() + '\n')

def display_projects(projects):
    """Display incomplete and completed projects."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]

    incomplete_projects.sort()
    completed_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in completed_projects:
        print(f"  {project}")

def filter_projects_by_date(projects):
    """Filter projects by start date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date > filter_date]
        filtered_projects.sort(key=lambda p: p.start_date)
        for project in filtered_projects:
            print(f"  {project}")
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def main():
    """main menu"""
    filename = 'projects.txt'
    projects = load_projects_from_file(filename)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {filename}")
    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")