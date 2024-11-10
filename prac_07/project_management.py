"""Estimate time: 40Mins
Actual time:1 hour"""
import datetime
from project import Project

def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]  # Skip header line
        for line in lines:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            projects.append(Project(name, datetime.datetime.strptime(start_date, "%d/%m/%Y").date(), int(priority), float(cost_estimate), int(completion_percentage)))
    return projects

def save_projects(filename, projects):
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

def add_new_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = datetime.datetime.strptime(input("Start date (dd/mm/yyyy): "), "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    print("Project added successfully!")

def update_project(projects):
    """Update a project's completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)
        new_completion_percentage = input("New completion percentage (leave blank to keep current): ")
        if new_completion_percentage:
            project.completion_percentage = int(new_completion_percentage)
        new_priority = input("New priority (leave blank to keep current): ")
        if new_priority:
            project.priority = int(new_priority)
        print("Project updated.")
    except (IndexError, ValueError):
        print("Invalid choice.")


def main():
    """main menu"""
    filename = 'projects.txt'
    projects = load_projects(filename)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {filename}")
    menu_option = None
    while menu_option != 'q':
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        menu_option = input(">>> ").lower()
        if menu_option == 'l':
            filename = input("Filename: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}.")
        elif menu_option == 's':
            filename = input("Filename: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}.")
        elif menu_option == 'd':
            display_projects(projects)
        elif menu_option == 'f':
            filter_projects_by_date(projects)
        elif menu_option == 'a':
            add_new_project(projects)
        elif menu_option == 'u':
            update_project(projects)
        elif menu_option == 'q':
            save_choice = input("Would you like to save to projects.txt? (yes/no): ").lower()
            if save_choice == 'yes':
                save_projects("projects.txt", projects)
                print("Projects saved to projects.txt.")
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()