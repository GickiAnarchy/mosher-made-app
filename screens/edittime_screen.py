import datetime
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers.datepicker import MDDockedDatePicker
from kivymd.uix.pickers.timepicker import MDTimePickerDialHorizontal
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty, StringProperty


class EditTimeScreen(MDScreen):
    selected_date = StringProperty("")
    selected_employee = StringProperty("Select Employee")
    selected_employer = StringProperty("Select Employer")
    time_in = StringProperty("08:00")
    time_out = StringProperty("17:00")

    _time_type = StringProperty("in") # Internal flag to distinguish between Time In/Out

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.employee_menu = None
        self.employer_menu = None

    def on_pre_enter(self):
        # Initialize default date to today if not set
        if not self.selected_date:
            self.selected_date = datetime.datetime.now().strftime("%m/%d/%Y")

    def open_employee_menu(self, caller):
        menu_items = [
            {
                "text": name,
                "on_release": lambda x=name: self.set_employee(x),
            } for name in self.app.rc.employees
        ]
        self.employee_menu = MDDropdownMenu(caller=caller, items=menu_items, width_mult=4)
        self.employee_menu.open()

    def set_employee(self, name):
        self.selected_employee = name
        if self.employee_menu:
            self.employee_menu.dismiss()

    def open_employer_menu(self, caller):
        menu_items = [
            {
                "text": name,
                "on_release": lambda x=name: self.set_employer(x),
            } for name in self.app.rc.employers
        ]
        self.employer_menu = MDDropdownMenu(caller=caller, items=menu_items, width_mult=4)
        self.employer_menu.open()

    def set_employer(self, name):
        self.selected_employer = name
        if self.employer_menu:
            self.employer_menu.dismiss()

    def edit_date(self, btn=None):
        date_dialog = MDDockedDatePicker()
        date_dialog.bind(on_ok=self.on_date_picker, on_cancel=lambda x: date_dialog.dismiss())
        date_dialog.open()

    def on_date_picker(self, instance, value):
        if value:
            # KivyMD 2.0 returns a list of date objects
            self.selected_date = value[0].strftime("%m/%d/%Y")
        instance.dismiss()

    def edit_time(self, time_type="in"):
        self._time_type = time_type
        time_dialog = MDTimePickerDialHorizontal()
        time_dialog.bind(on_ok=self.on_time_picker, on_cancel=lambda x: time_dialog.dismiss())
        time_dialog.open()
    
    def on_time_picker(self, instance):
        time_val = instance.time.strftime("%H:%M")
        if self._time_type == "in":
            self.time_in = time_val
        else:
            self.time_out = time_val
        instance.dismiss()

    def save_shift(self):
        if "Select" in self.selected_employee or "Select" in self.selected_employer:
            print("Error: Employee and Employer must be selected.")
            return

        # Assumes a note field exists in KV with id: note_field
        note = self.ids.note_field.text if 'note_field' in self.ids else ""
        
        self.app.rc.time_manager.log_shift(
            date=self.selected_date,
            employee_name=self.selected_employee,
            employer_name=self.selected_employer,
            time_in=self.time_in,
            time_out=self.time_out,
            note=note
        )
        self.manager.current = "home"

    @property
    def app(self):
        return MDApp.get_running_app()
