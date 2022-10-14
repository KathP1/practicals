"""
Wimbeldon
Estimate: 45 minutes
Actual:
"""

FILENAME = 'wimbledon.csv'
INDEX_COUNTRY = 1


def main():
    records = load_data(FILENAME)
    print(records)
    """Create a dictionary to store champion and the count of occurrences in the 'Champion' column of the data"""
    champion_to_count = {}  # empty dictionary to store champions and number of wins
    for record in records:
        try:
            champion_to_count[record[2]] += 1  # if champion (index 2) is in the dict increase count by 1
        except KeyError:
            champion_to_count[record[2]] = 1  # if champion isn't in the list add it and commence count at 1
    print(champion_to_count)
    print(f" This is {type(champion_to_count)}")
    """Create a set of countries"""
    countries = set()  # empty set to store a set of unique country names
    for record in records:
        countries.add(record[1])  # Add Country (index 1) to the list
    print(countries, type(countries))
    number_of_countries = len(countries)
    print("Wimbeldon Champions:")
    for champion in champion_to_count:
        print(f"{champion}: {champion_to_count[champion]}")
    print(f"These {number_of_countries} countries have won Wimbledon")
    print(', '.join(countries))
    # for champion in records:
    #     try:
    #         champion_to_count[champion] += 1
    #     except KeyError:
    #         champion_to_count = 1
    # print(champion_to_count)
    # count_champions
    # list_of_countries


def load_data(filename):
    """read records from a file and store as a list of lists"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Read one line before loop to remove header
        for line in in_file:
            # print(line[-1], type(line))
            parts = line.strip().split(",")  # split into a list of strings
            # print(parts[1])
            records.append(parts)  # add records to the list to make a list of lists
            # print(parts)
        return records



# def sort_countries(countries):
#     pass
#
#
# def display details(countries):
#     pass

main()
