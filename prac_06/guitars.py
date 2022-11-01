"""
A program to store and display a user's guitars
Estimated time: 90 minutes
Actual time:
"""

from guitar import Guitar


def main():
    """Get information on guitars and display their details"""
    guitars =[]
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar)
        name = input("Name: ")

    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)


main()

