"""
CP1404 Practical 09
Band class
"""

from prac_09.musician import Musician


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
        """Return a string showing the musician playing their first (or no) instrument."""
        # # musicians_play = Musician.play(Musician.__repr__())
        # # musicians = [str(musician) for musician in self.musicians]
        # # musicians2 = [musician for musician in self.musicians]
        # print(self.musicians)
        # if not self.instruments:
        #     return f"{self.name} needs an instrument!"
        # return f"{self.name} is playing: {self.instruments[0]}"
        #
        # # print(musicians)
        # # print(musicians2)
        # # musicians.play()
        # # print(musicians)
        # # return musicians

        for musician in self.musicians:
            if not musician.instruments:
                self.plays.append(f"{musician.name} needs an instrument")
            else:
                self.plays.append(f"{musician.name} plays {musician.instruments[0]}")
        musician_plays = '\n'.join([play for play in self.plays])
        return musician_plays

