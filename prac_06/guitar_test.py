"""
Testing for get_age and is_vintage methods
"""

from guitar import Guitar


def main():
    """Test that get_age and is_vintage methods work"""
    gibson = Guitar("Gibson L-5 CES", 1922, 15000)
    another_guitar = Guitar("Another guitar", 2013, 4000)
    print(gibson)
    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


main()
