"""
CP1404 Practical 08
Kivy GUI program to convert miles to kilometers
Estimated time: 8hrs
Actual time:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


class ConvertMilesApp(App):
    """ConvertMilesApp is a Kivy App for converting miles to kilometers"""
    message = StringProperty()

    def build(self):
        """build the Kivy app from the kv file"""
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = ""
        return self.root

    def handle_update(self):
        """Handle changes to the text input by updating the model from the view."""
        self.message = self.root.ids.output_label.text

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = float(value) * 1.609344
        self.root.ids.output_label.text = str(f"{result:.3f}")


ConvertMilesApp().run()
