"""
Make a simple class for a programming language
Estimated time: 1 hour
Actual time: 1 hour
"""


class ProgrammingLanguage:
    """Information about programming language"""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgramingLanguage instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage object"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return True or False if the programming language is dynamically typed or not"""
        return self.typing == "Dynamic"
