"""
CP1404 Practical 07
Guitars
"""

from prac_07.guitar import Guitar


def main():
    """Read file of guitar details, save as a list of objects, display."""
    guitars = load_guitars()
    add_guitar(guitars)
    if guitars:
        display_guitars(guitars)
    else:
        print("No guitars")
    save_guitars(guitars)


def save_guitars(guitars):
    """Save guitars to a file"""
    with open('guitars.csv', 'w', encoding="utf-8-sig") as out_file:
        for guitar in guitars:
            print(repr(guitar), file=out_file)


def display_guitars(guitars):
    """Display guitars sorted from oldest to youngest"""
    guitars.sort()
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        print(f"Guitar {i}: {guitar}{vintage_string}")


def add_guitar(guitars):
    """Get user input to add guitar details"""
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")


def load_guitars():
    """Open guitars file and store as a list of lists"""
    guitars = []
    with open('guitars.csv', 'r', encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


main()
