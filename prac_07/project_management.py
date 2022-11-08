"""
CP1404 - Prac 07 - Project Management
Time Estimate:5hrs
Actual time:
"""

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
    projects = load_projects(FILENAME)
    print(MENU_STRING)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
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
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        print(project)
        projects.append(project)
    in_file.close()


main()
