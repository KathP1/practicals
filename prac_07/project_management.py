"""
CP1404 - Prac 07 - Project Management
A program to load and save a data file and use a list of Project objects
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
    """Get a date from the user and display projects starting on or after that date"""
    is_valid_input = False
    while not is_valid_input:
        try:
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filtered = [project for project in projects if project.start_date >= filter_date]
            filtered.sort(key=attrgetter("start_date"))
            for project in filtered:
                print(project)
            is_valid_input = True
        except ValueError:
            print("Invalid input; enter a date in the format specified")


def add_new_project(projects):
    """Prompt user for project details and add to the list of projects"""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority: ")
    # priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = get_valid_number("Percent complete: ")
    # percent_complete = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(new_project)


def update_project(projects):
    """Get index of project and update completion percent &/or priority"""
    chosen_index = choose_project(projects)
    # print(projects[chosen_index])
    new_percentage = input("New Percentage: ")
    if new_percentage.isdigit():
        projects[chosen_index].completion_percentage = int(new_percentage)
    new_priority = input("New Priority: ")
    if new_priority.isdigit():
        projects[chosen_index].priority = int(new_priority)


def choose_project(projects):
    """Get index of project to update"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    is_valid_input = False
    while not is_valid_input:
        try:
            chosen_index = get_valid_number("Project choice: ")
            print(projects[chosen_index])
            is_valid_input = True
            return chosen_index
        except IndexError:
            print("Invalid project number")
        # except ValueError:
        #     print("Please enter an integer")


def get_valid_number(user_prompt):
    """Ask for a number and check if it is valid"""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(user_prompt))
            is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return number


main()
