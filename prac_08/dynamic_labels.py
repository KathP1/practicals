"""
CP1404 Practical 08
Kivy GUI program to display a list of names as separate labels
Estimated time: 4 hrs
Actual time: 30 mins!
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """DynamicLabelsApp is a Kivy App to display a list of names"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from dictionary entries and add them to the GUI."""
        for name in self.name_to_phone:
            # create a label for each data entry, specifying the text and id
            temp_label = Label(text=name)
            # add the label to the "main" layout widget
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
