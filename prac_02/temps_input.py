"""Get 15 random floats between -200 and 200
write to a text file called temps_input.txt"""

import random


def main():
    number_of_temperature_values = 15
    out_file = open('temps_input.txt', 'w')
    for i in range(number_of_temperature_values):
        temperature = random.uniform(-200, 200, )
        out_file.write(str(temperature) + "\n")
    out_file.close()
    results_file = open('temps_input.txt', 'r')
    print(results_file.read())


main()
