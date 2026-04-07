import os
import json

from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton,MDButtonText
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ListProperty, DictProperty, StringProperty, ObjectProperty
from kivymd.app import MDApp
from data import CheckItem



class TimeClockScreen(MDScreen):
    employees = ListProperty()
    clocked_in_employees = DictProperty()
    check_items = ListProperty()
    employers = ListProperty()
    selected_employer = StringProperty("Select Employer")
    employer_menu = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    def on_enter(self):
        try:
            self.employees = self.app.rc.employees
        except Exception as e:
            print(e)

        self.get_currently_clocked_in()
        self.get_employers()
        self.update_employees()
    

    def get_employers(self):
        self.employers = self.app.rc.employers
    

    def get_currently_clocked_in(self):
        if os.path.exists("clocked_in.json"):
            try:
                with open("clocked_in.json", "r") as f:
                    self.clocked_in_employees = json.load(f)
            except json.JSONDecodeError:
                self.clocked_in_employees = {}


    def on_employees(self, instance, value):
        """Triggered automatically when the bound list updates."""
        self.update_employees()


    def update_employees(self):
        self.ids.check_items_container.clear_widgets()
        self.check_items.clear()
        
        if not self.employees:
            print("No employees to display.")
            check_item = CheckItem(text="No employees found")
            self.ids.check_items_container.add_widget(check_item)
            self.check_items.append(check_item)
            return

        for employee in self.employees:
            check_item = CheckItem(text=employee)
            if employee in self.clocked_in_employees:
                check_item.checkbox.active = True
            self.ids.check_items_container.add_widget(check_item)
            self.check_items.append(check_item)


    def open_employer_menu(self, caller):
        """Creates and opens the employer selection menu."""
        menu_items = [
            {
                "text": name,
                "on_release": lambda x=name: self.set_employer(x),
            } for name in self.employers
        ]
        self.employer_menu = MDDropdownMenu(
            caller=caller,
            items=menu_items,
        )
        self.employer_menu.open()


    def set_employer(self, employer_name):
        """Sets the selected employer and closes the menu."""
        self.selected_employer = employer_name
        if self.employer_menu:
            self.employer_menu.dismiss()


    def get_selected_employees(self):
        """Returns a list of employee names that are currently checked."""
        return [item.name_text for item in self.check_items if item.checkbox.active and item.name_text != "No employees found"]


    def handle_clock_in(self):
        """Example trigger method to be called from a button in your KV file."""
        now = self.app.rc.time_manager.get_current_time()
        selected = self.get_selected_employees()
        if not selected:
            print("No employees selected for Clock In.")
            return

        # Update local status and persist to file
        for employee in selected:
            self.clocked_in_employees[employee] = now
        
        with open("clocked_in.json", "w") as f:
            json.dump(dict(self.clocked_in_employees), f)

        print(f"Clocking in: {selected}")
        self.update_employees()


    def handle_clock_out(self):
        """Example trigger method to be called from a button in your KV file."""
        if self.selected_employer == "Select Employer":
            print("Error: No employer selected.")
            return

        selected = self.get_selected_employees()
        clock_out_time = self.app.rc.time_manager.get_current_time()

        if not selected:
            print("No employees selected for Clock Out.")
            return

        for employee in selected:
            if employee in self.clocked_in_employees:
                clock_in_time = self.clocked_in_employees[employee]
                self.app.rc.time_manager.log_shift(
                    date=None, 
                    employee_name=employee, 
                    employer_name=self.selected_employer, 
                    time_in=clock_in_time, 
                    time_out=clock_out_time
                )

                del self.clocked_in_employees[employee]
        
        # Update the file after removing employees
        with open("clocked_in.json", "w") as f:
            json.dump(dict(self.clocked_in_employees), f)

        print(f"Clocking out: {selected}")
        self.update_employees()


    @property
    def app(self):
        return MDApp.get_running_app()