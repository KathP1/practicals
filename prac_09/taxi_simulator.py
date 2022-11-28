"""
CP1404 Practical 09
A taxi simulator program that uses Taxi and SilverServiceTaxi classes
Estimated time: 5hrs
Actual time: 5hrs
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU_STRING = "q)uit, c)hoose taxi, d)rive"


def main():
    """A taxi simulator that gets a choice of taxi and distance, and calculates trip cost"""
    prius = Taxi("prius", 100)
    limo = SilverServiceTaxi("Limo", 100, 2)
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    taxis = [prius, limo, hummer]
    current_taxi = None
    bill_to_date = 0
    print("Let's drive")
    print(MENU_STRING)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)
        elif choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill_to_date = drive_taxi(bill_to_date, current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU_STRING)
        choice = input(">>> ").upper()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display taxis"""
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")


def get_valid_number():
    """Get valid taxi number"""
    is_valid_input = False
    while not is_valid_input:
        try:
            taxi_number = int(input("Choose taxi: "))
            if taxi_number < 0:
                print("Number must be >= 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return taxi_number


def choose_taxi(taxis):
    """Get index of chosen taxi and allocate as the current_taxi"""
    try:
        taxi_number = get_valid_number()
        current_taxi = taxis[taxi_number]
    except IndexError:
        print("Invalid taxi choice")
        current_taxi = None
    return current_taxi


def get_drive_distance():
    """Get valid drive distance."""
    is_valid_input = False
    while not is_valid_input:
        try:
            driven_distance = float(input("Drive how far? "))
            if driven_distance < 0:
                print("Invalid number")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return driven_distance


def drive_taxi(bill_to_date, current_taxi):
    """Drive taxi."""
    current_taxi.start_fare()
    driven_distance = get_drive_distance()
    current_taxi.drive(driven_distance)
    print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
    bill_to_date += current_taxi.get_fare()
    return bill_to_date


main()
