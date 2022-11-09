"""
CP1404 - Prac 07 - Project Management
Time Estimate:5hrs
Actual time:
"""
from operator import attrgetter

import datetime

from prac_07.project import Project

FILENAME = "projects.txt"
HEADER = ["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"]
MENU_STRING = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """Manage a project list-display, filter, add new, update details, save to a file"""
    projects = load_projects(FILENAME)
    print(MENU_STRING)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Projects file to load (filename.txt): ")
            projects = load_projects(filename)
        elif choice == "S":
            save_file = input("Save changes to (filename.txt): ")
            save_projects(save_file, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            display_filtered(projects)
        elif choice == "A":
            print("Let's add a new project")
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU_STRING)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software")


def load_projects(filename):
    """Open project file and store as a list of lists"""
    projects = []
    with open(filename, 'r', encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip()
            parts = line.split("\t")
            # print(parts)  #checking
            parts[2] = int(parts[2])
            parts[3] = float(parts[3])
            parts[4] = int(parts[4])
            # print(parts) #checking
            date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            project = Project(parts[0], date, parts[2], parts[3], parts[4])
            # print(project)  # checking
            # print(type(project.start_date)) #checking
            # print(project.start_date) #checking
            # print(project2.start_date) #checking
            projects.append(project)
        # in_file.close()
    return projects


def save_projects(save_file, projects):
    """Save list of projects to a file"""
    print(f"V2:{projects}")
    with open(save_file, 'w', encoding="utf-8-sig") as out_file:
        for heading in HEADER:
            print(heading, file=out_file, end="\t")
        out_file.write('\n')
        for project in projects:
            print(repr(project), file=out_file)
    # out_file.close()


def display_projects(projects):
    """Display incomplete and complete projects sorted by priority"""
    incomplete_projects = [project for project in projects if project.completion_percentage != 100]
    incomplete_projects.sort(key=attrgetter("priority"))
    complete_projects = [project for project in projects if project.completion_percentage == 100]
    complete_projects.sort(key=attrgetter("priority"))
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)
    print("Completed projects:")
    for project in complete_projects:
        print(project)


def display_filtered(projects):
    """Gets a threshold date from the user and displays projects with start date >= to that date"""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_from_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date >= filter_from_date]
    filtered_projects.sort(key=attrgetter("start_date"))
    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """Prompt user for project details and add to the list of projects"""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(new_project)


def update_project(projects):
    """Get index of project and update completion percent &/or priority"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    chosen_index = int(input("Project choice: "))
    print(projects[chosen_index])
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_percentage != "":
        projects[chosen_index].completion_percentage = int(new_percentage)
    if new_priority != "":
        projects[chosen_index].priority = int(new_priority)


main()
