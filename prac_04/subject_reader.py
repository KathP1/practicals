"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    # print(data)
    display_subject_details(data)


def display_subject_details(data):
    """Display the subject details in a sentence"""
    for subject_details in data:
        print(f"{subject_details[0]} is taught by {subject_details[1]} and has {subject_details[2]} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        subject_data.append(parts)
        # print(subject_data)
        # print("----------")
    input_file.close()
    return subject_data


main()
