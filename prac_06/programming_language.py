"""
Make a simple class for a programming language
Estimated time: 1 hour
Actual time:
"""


class ProgrammingLanguage:
    """Information about programming language"""

    def __init__(self, typing="", reflection="", year=0):
        """Initialise a ProgramingLanguage instance"""
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True or False if the programming language is dynamically typed or not"""
        return self.typing == "Dynamic"

