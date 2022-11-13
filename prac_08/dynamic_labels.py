"""
CP1404 Practical 08
Kivy GUI program to display a list of names as separate labels
Estimated time: 4hrs
Actual time:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """DynamicLabelsApp is a Kivy App to display a list of names"""
    status_text = StringProperty()

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        # self.create_widgets()
        return self.root


DynamicLabelsApp().run()
