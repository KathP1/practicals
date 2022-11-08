"""
A class to store information for a guitar
Estimated time: 90 minutes
Time taken: 30 minutes
"""
from datetime import date


class Guitar:
    """Represent information about a guitar"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"


    def get_age(self):
        """Extract the age of the Guitar"""
        current_year = date.today().year
        age = current_year - self.year
        return age

    def is_vintage(self):
        """Determines if Guitar is more than 50 years old"""
        return self.get_age() >= 50

    def __lt__(self, other):

