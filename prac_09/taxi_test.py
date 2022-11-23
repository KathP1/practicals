"""
CP1404 Practical 09
Testing taxi class
"""

from prac_09.taxi import Taxi


def main():
    """Test Taxi class"""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(f"{my_taxi}, current fare: ${my_taxi.get_fare():.2f}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    # Note: taxi couldn't drive 100km because there was only 60 units of fuel left
    print(f"{my_taxi}, current fare: ${my_taxi.get_fare():.2f}")


main()
