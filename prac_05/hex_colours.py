"""
CP1404/CP5632 Practical
hexadecimal colour codes in a dictionary
"""

COLOUR_TO_CODE = {"Red": "#FF0000", "Orange": "#FFA500", "Yellow": "#FFFF00", "Green": "#00FF00",
                  "Blue": "#0000FF", "Indigo": "#4B0082", "Violet": "#8F00FF"}
for colour in COLOUR_TO_CODE:
    print(f"Hexadecimal code for {colour:6} is: {COLOUR_TO_CODE[colour]}")

colour = input("Enter colour: ").upper().title()
while colour != "":
    try:
        print(colour, "is", COLOUR_TO_CODE[colour])
    except KeyError:
        print("Invalid colour")
    colour = input("Enter colour: ").title()
