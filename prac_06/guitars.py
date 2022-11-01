"""
A program to store and display a user's guitars
Estimated time: 90 minutes
Actual time:
"""

from guitar import Guitar


def main():
    """Get information on guitars and display their details"""
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        print(guitar)
        name = input("Name: ")

    print("These are my guitars:")


main()

