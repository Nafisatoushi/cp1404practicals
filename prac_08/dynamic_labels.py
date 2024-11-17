"""Estimate time:40 min
Actual time: """

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main application class for dynamically creating labels."""


    def __init__(self, **kwargs):
        """Construct the app."""
        super().__init__(**kwargs)
        # List of names
        self.names = ["Alice", "Bob", "Charlie", "David", "Emily"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"  # Set window title
        self.root = Builder.load_file('dynamic_labels.kv')  # Load KV file
        self.create_labels()
        return self.root