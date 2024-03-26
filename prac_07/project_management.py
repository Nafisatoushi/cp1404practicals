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
def save_projects(projects, filename="projects.txt"):
    """Save projects to the specified file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file, delimiter="\t")
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([project.name, project.start_date, project.priority, project.cost_estimate, project.completion_percentage])
def main():
    """Main function to manage projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    print(f"Loaded {len(projects)} projects from projects.txt")

main()
# Main menu
while True:
    print("\nMain Menu:")
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

    choice = input("Enter your choice: ").strip().lower()

    if choice == "l":
        print("Load projects functionality will be implemented in a later step")
    elif choice == "s":
        save_projects(projects)
        print("Projects saved successfully.")
    elif choice == "d":
        display_projects(projects)
    elif choice == "f":
        filter_projects_by_date(projects)
    elif choice == "a":
        add_new_project(projects)
    elif choice == "u":
        update_project(projects)
    elif choice == "q":
        save_choice = input("Would you like to save to projects.txt? ").strip().lower()
        if save_choice.startswith("y"):
            save_projects(projects)
            print("Projects saved successfully.")
        print("Thank you for using custom-built project management software.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

main()