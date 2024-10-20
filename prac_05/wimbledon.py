import csv

def read_csv(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip header row
        for row in reader:
            data.append(row)
    return data