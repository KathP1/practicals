"""
CP1404 Practical 07
Guitars
"""

from prac_07.guitar import Guitar


def main():
    """Read file of guitar details, save as a list of objects, display."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        # print(repr(line))  # debugging
        parts = line.strip().split(',')
        # print(parts)  # debugging
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    # Loop through and display all guitars
    for guitar in guitars:
        print(guitar)


main()
