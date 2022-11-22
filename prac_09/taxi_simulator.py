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
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU_STRING)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            display_taxis(taxis)
            choose_taxi(taxis)
        elif choice == "D":
            pass
        else:
            print("Invalid menu choice")
        print(MENU_STRING)
        choice = input(">>> ").upper()
    print(f"Total trip cost: $")


def display_taxis(taxis):
    """display_taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i} {taxi}")


def choose_taxi(taxis):
    """Get index of chosen taxi"""
    is_valid_input = False
    while not is_valid_input:
        try:
            chosen_taxi = get_valid_number("Choose taxi: ")
            current_taxi = taxis[chosen_taxi]
            # print(taxis[chosen_taxi]) #Debugging
            # print(f"current taxi: {current_taxi}") #Debugging
            is_valid_input = True
            return current_taxi
        except IndexError:
            print("Invalid taxi choice")


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
