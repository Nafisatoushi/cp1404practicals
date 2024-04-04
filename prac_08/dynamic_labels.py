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

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            # Create a label for each name
            temp_label = Label(text=name)
            # Add the label to the "main" layout widget
            self.root.ids.main.add_widget(temp_label)

# Run the app
DynamicLabelsApp().run()



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
        main_layout = BoxLayout(orientation='vertical', id='main')
        self.create_labels(main_layout)
        return main_layout
    def create_labels(self, layout):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            # Create a label for each name
            temp_label = Label(text=name)
            # Add the label to the layout widget
            layout.add_widget(temp_label)

# Run the app
DynamicLabelsApp().run()
