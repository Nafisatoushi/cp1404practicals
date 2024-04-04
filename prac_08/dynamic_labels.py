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

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"  # Set window title
        self.root = Builder.load_file('dynamic_labels.kv')  # Load KV file
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            # Create a label for each name
            temp_label = Label(text=name)
            # Add the label to the "labels_box" layout widget
            self.root.ids.labels_box.add_widget(temp_label)