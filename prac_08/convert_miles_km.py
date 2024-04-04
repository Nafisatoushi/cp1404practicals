"""Estimate time: 3hours
actual time: """
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    output_text = StringProperty("")

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km_solution.kv')
        self.output_text = "Type in the field & press Enter"
        return self.root
