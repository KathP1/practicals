"""
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    temps_input = open('temps_input.txt', 'r')
    temps_output = open('temps_output.txt', 'w')
    while choice != "Q":
        if choice == "F":
            for line in temps_input:
                fahrenheit = float(line)
                celsius = 5.0 / 9.0 * (fahrenheit - 32)
                print(celsius, file=temps_output)
            temps_output.close()


main()
