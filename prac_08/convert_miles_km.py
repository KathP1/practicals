"""
CP1404 Practical 08
Kivy GUI program to convert miles to kilometers
Estimated time: 8hrs
Actual time:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesApp(App):
    """ConvertMilesApp is a Kivy App for converting miles to kilometers"""

    def build(self):
        """build the Kivy app from the kv file"""
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesApp().run()
