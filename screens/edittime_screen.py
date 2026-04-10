from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDButton,MDButtonText
from kivymd.uix.pickers import MDTimePickerInput, MDModalInputDatePicker
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
from kivy.clock import Clock


class EditTimeScreen(MDScreen):
    time_picker = ObjectProperty()
    date_picker = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time_picker = MDTimePickerInput()
        self.time_picker.bind(on_time_input=self.on_time_picker)
        self.date_picker = MDModalInputDatePicker()
        self.date_picker.bind(on_ok=self.on_date_picker)


    
    def on_time_picker(self, instance, value, is_error = False):
        print(f"Chose time: {value}, Error: {is_error}")


    def on_date_picker(self, instance, value, is_error = False):
        print(f"Chose date: {self.date_picker.get_date()}")


    def edit_time(self, btn = None):
        self.time_picker.open()


    def edit_date(self, btn = None):
        self.date_picker.open()



    @property
    def app(self):
        return MDApp.get_running_app()