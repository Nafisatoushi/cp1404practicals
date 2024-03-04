import csv

def read_csv(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip header row
        for row in reader:
            data.append(row)
    return data

def process_data(data):
    champions = {}
    countries = set()
    for row in data:
        champion = row[2]
        country = row[1]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
        countries.add(country)
    return champions, sorted(countries)

def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

def display_countries(countries):
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(countries))

def main():
    filename = "wimbledon.csv"
    data = read_csv(filename)
    champions, countries = process_data(data)
    display_champions(champions)
    display_countries(countries)


main()