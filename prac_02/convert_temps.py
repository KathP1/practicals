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
        if choice == "C":
            convert_celsius_to_fahrenheit(temps_input, temps_output)
        if choice == "F":
            convert_fahrenheit_to_celsius(temps_input, temps_output)


def convert_fahrenheit_to_celcius(temps_input, temps_output):
    for line in temps_input:
        fahrenheit = float(line)
        celsius = 5.0 / 9.0 * (fahrenheit - 32)
        print(celsius, file=temps_output)
    temps_output.close()


def convert_celsius_to_fahrenheit(temps_input, temps_output):
    for line in temps_input:
        celsius = float(line)
        fahrenheit = celsius * 9.0 / 5 + 32
        print(fahrenheit, file=temps_output)
    temps_output.close()

main()
