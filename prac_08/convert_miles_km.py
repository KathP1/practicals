"""
CP1404 Practical 08
Kivy GUI program to convert miles to kilometers
Estimated time: 8hrs
Actual time: 2.5hrs
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.609344


class ConvertMilesApp(App):
    """ConvertMilesApp is a Kivy App for converting miles to kilometers"""

    # message = StringProperty()

    def build(self):
        """build the Kivy app from the kv file"""
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        # self.message = ""
        return self.root

    def handle_calculate(self):
        """handle calculation, display result in label """
        result = self.get_valid_miles() * MILES_TO_KM
        self.root.ids.output_label.text = str(f"{result:.3f}")

    def handle_increment(self, increment):
        """Handle up/down button press, increment the miles value +- 1"""
        value = self.get_valid_miles() + increment
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_valid_miles(self):
        """Get valid number for miles or return 0 if not valid"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0



ConvertMilesApp().run()
