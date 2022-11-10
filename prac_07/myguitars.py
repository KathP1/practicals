"""
CP1404 Practical 07
Guitars
"""

from prac_07.guitar import Guitar


def main():
    """Read file of guitar details, save as a list of objects, display."""
    guitars = load_guitars()
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage_string))
    else:
        print("No guitars")

    with open('guitars.csv', 'w', encoding="utf-8-sig") as out_file:
        for guitar in guitars:
            print(repr(guitar), file=out_file)


def load_guitars():
    """Open guitars file and store as a list of lists"""
    guitars = []
    in_file = open('guitars.csv', 'r', encoding="utf-8-sig")
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars


main()
