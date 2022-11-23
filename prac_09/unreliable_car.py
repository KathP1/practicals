"""
CP1404 Practical 09
Unreliable car class
"""
from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability
        self.current_distance = 0

    def __str__(self):
        """Return a string like a Car but with current distance."""
        return f"{super().__str__()}, drove {self.current_distance}km"

    def drive(self, distance):
        """Drive like parent Car but only if a random number
        between 0 and 100 is less than car's reliability."""
        distance_driven = super().drive(distance)
        if randint(0, 100) < self.reliability:
            self.current_distance += distance_driven
        return distance_driven
