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
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: "))
        completion_percentage = int(input("Percent complete: "))
        projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        print("New project added.")
    except ValueError:
        print("Invalid input format.")