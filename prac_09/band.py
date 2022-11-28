"""
CP1404 Practical 09
Band class
"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a musician."""
        self.name = name
        self.musicians = []
        self.plays = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join([str(musician) for musician in self.musicians])})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to a band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first (or no) instrument."""
        for musician in self.musicians:
            if not musician.instruments:
                self.plays.append(f"{musician.name} needs an instrument")
            else:
                self.plays.append(f"{musician.name} plays {musician.instruments[0]}")
        musician_plays = '\n'.join(self.plays)
        return musician_plays
