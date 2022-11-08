"""Get 15 random floats between -200 and 200
write to a text file called temps_input.txt"""

import random


def main():
    """Generate a series of floats between a specified range"""
    number_of_temperature_values = 15
    out_file = open('temps_input.txt', 'w', encoding="utf8")
    for temperature in range(number_of_temperature_values):
        temperature = random.uniform(-200, 200, )
        out_file.write(str(temperature) + "\n")
    out_file.close()
    results_file = open('temps_input.txt', 'r', encoding="utf8")
    print(results_file.read())


main()
