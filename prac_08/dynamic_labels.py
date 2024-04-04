from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class DynamicLabelsApp(App):
    """Main application class for dynamically creating labels."""
    status_text = StringProperty()  # Property for status text

    def __init__(self, **kwargs):
        """Construct the app."""
        super().__init__(**kwargs)
        # List of names
        self.names = ["Alice", "Bob", "Charlie", "David", "Emily"]