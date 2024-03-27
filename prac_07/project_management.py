import datetime
from project import Project

def load_projects_from_file(filename):
    projects = []
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]  # Skip header line
        for line in lines:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            projects.append(Project(name, datetime.datetime.strptime(start_date, "%d/%m/%Y").date(), int(priority), float(cost_estimate), int(completion_percentage)))
    return projects

def save_projects_to_file(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")  # Header
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda x: x.priority):
        print(f"  {project}")

def filter_projects_by_date(projects):
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date > date]
        for project in sorted(filtered_projects, key=lambda x: x.start_date):
            print(f"  {project}")
    except ValueError:
        print("Invalid date format. Please use the format dd/mm/yyyy.")


def add_new_project(projects):
    """Add a new project to the list."""
    name = input("Enter the name of the project: ")
    date_string = input("Enter the start date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    print(f"That day is/was {date.strftime('%A')}")
    priority = int(input("Enter the priority: "))
    cost_estimate = float(input("Enter the cost estimate: "))
    completion_percentage = float(input("Enter the completion percentage: "))

    project = Project(name, date, priority, cost_estimate, completion_percentage)
    projects.append(project)
    print("Project added successfully.")

def update_project(projects):
    display_projects(projects)
    project_choice = input("Project choice: ")
    try:
        project_choice = int(project_choice)
        if 0 <= project_choice < len(projects):
            project = projects[project_choice]
            new_completion_percentage = input("New Percentage: ")
            if new_completion_percentage:
                project.completion_percentage = int(new_completion_percentage)
            new_priority = input("New Priority: ")
            if new_priority:
                project.priority = int(new_priority)
            print("Project updated.")
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Invalid input.")

def main():
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
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects_from_file(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects_to_file(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? (yes/no): ").lower()
            if save_choice == 'yes':
                save_projects_to_file('projects.txt', projects)
                print(f"Saved {len(projects)} projects to projects.txt")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()
