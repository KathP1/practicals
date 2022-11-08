"""
CP1404 - Prac 07 - Project Management
Time Estimate:5hrs
Actual time:
"""
from operator import attrgetter

from prac_07.project import Project

FILENAME = "projects.txt"
MENU_STRING = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """Manage a list of projects - display projects, filter, add new projects, update details, and save to a file"""
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
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(MENU_STRING)
        choice = input(">>> ").upper()


def load_projects(filename):
    """Open project file and store as a list of lists"""
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()
    for line in in_file:
        line = line.strip()
        parts = line.split("\t")
        # print(parts)  #checking
        parts[2] = int(parts[2])
        parts[3] = float(parts[3])
        parts[4] = int(parts[4])
        # print(parts) #checking
        # TODO Convert start date from string to date format
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        print(project)  # checking
        projects.append(project)
    in_file.close()
    return projects


def save_projects(save_file, projects):
    """Save list of projects to a file"""
    print(f"V2:{projects}")
    out_file = open(save_file, 'w')
    for project in projects:
        print(repr(project), file=out_file)
    out_file.close()


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


main()
