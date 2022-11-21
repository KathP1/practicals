"""
CP1404 Practical 09
A taxi simulator program that uses Taxi and SilverServiceTaxi classes
Estimated time: 5hrs
Actual time:
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU_STRING = "q)uit, c)hoose taxi, d)rive"


def main():
    """A taxi simulator that gets a choice of taxi and distance, and calculates trip cost"""
    print("Let's drive!")
    print(MENU_STRING)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
        elif choice == "D":
            pass
        else:
            print("Invalid menu choice")
        print(MENU_STRING)
        choice = input(">>> ").upper()
    print(f"Total trip cost: $")


main()
