"""
Wimbeldon
Estimate: 45 minutes
Actual:
"""

FILENAME = 'wimbledon.csv'


def main():
    load_data(FILENAME)
    # count_champions
    # list_of_countries
    pass


def load_data(filename):
    """Get records from a file and """
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove header
        for line in in_file:
            # print(line[-1], type(line))
            parts = line.strip(",")  # strip the white space from the end
            parts = parts.split(",") # split into a list of strings
            # print(parts[1])
            records.append(parts) # add records to the list to make a list of lists
            print(parts)
        # return records


# def sort_countries(countries):
#     pass
#
#
# def display details(countries):
#     pass

main()
