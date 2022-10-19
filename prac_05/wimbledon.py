"""
Wimbeldon
Estimate: 45 minutes
Actual: 2.5 hours
"""

FILENAME = 'wimbledon.csv'

def main():
    """Read data and display champions and countries that have won Wimbledon"""
    records = load_data(FILENAME)
    champion_to_count, countries, number_of_countries = process_records(records)
    display_results(champion_to_count, countries, number_of_countries)


def display_results(champion_to_count, countries, number_of_countries):
    """Display champions and number of wins,  and sort and display winning countries"""
    print("Wimbeldon Champions:")
    for champion in champion_to_count:
        print(f"{champion}: {champion_to_count[champion]}")
    print(f"These {number_of_countries} countries have won Wimbledon")
    print(', '.join(sorted(countries)))


def process_records(records):
    """Create a dictionary to store champions and a set to store countries"""
    champion_to_count = {}  # empty dictionary to store champions and number of wins
    for record in records:
        try:
            champion_to_count[record[2]] += 1  # if champion (index 2) is in the dict increase count by 1
        except KeyError:
            champion_to_count[record[2]] = 1  # if champion isn't in the list add it and commence count at 1
    countries = set()  # empty set to store a set of unique country names
    for record in records:
        countries.add(record[1])  # Add Country (index 1) to the list
    number_of_countries = len(countries)
    return champion_to_count, countries, number_of_countries


def load_data(filename):
    """read records from a file and store as a list of lists"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Read one line before loop to remove header
        for line in in_file:
            parts = line.strip().split(",")  # split into a list of strings
            records.append(parts)  # add records to the list to make a list of lists
        return records

main()
