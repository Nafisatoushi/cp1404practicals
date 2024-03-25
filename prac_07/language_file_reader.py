"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    in_file = open('languages.csv', 'r')
    # File format is like: Language,Typing,Reflection,Year
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    # All other lines are language data
    for line in in_file:
        parts = line.strip().split(',')
        reflection = parts[2] == "Yes"
        # Extract pointer arithmetic from the row
        pointer_arithmetic = parts[9] == "Yes"
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
        languages.append(language)
    in_file.close()

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)

# main()

def using_namedtuple():
    """Language file reader version using a named tuple."""
    in_file = open('languages.csv', 'r', newline='')
    file_field_names = in_file.readline().strip().split(',')
    print(file_field_names)
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    reader = csv.reader(in_file)

    for row in reader:
        language = Language._make(row)
        print(repr(language))
    in_file.close()

def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    in_file = open("languages.csv", "r")
    in_file.readline()
    for language in map(Language._make, csv.reader(in_file)):
        print(language.name, 'was released in', language.year)
        print(repr(language))

# using_csv_namedtuple()
