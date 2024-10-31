"""
Programming Language
Estimate: 30 minutes
Actual:   40 minutes
"""

class ProgrammingLanguage:class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year


    def is_dynamic(self):
        return self.typing.lower() == 'dynamic'


