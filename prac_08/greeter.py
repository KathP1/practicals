from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.graphics import Color


class BoxLayoutDemo(App):
    def build(self):
        """Set up a GUI to greet a person by entered name"""
        Window.size = (700, 300)
        self.title = "Greeter Program"
        self.root = Builder.load_file('greeter.kv')
        return self.root

    def handle_greet(self):
        """Print a statement when Greet button is pressed"""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear entered and displayed values"""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
