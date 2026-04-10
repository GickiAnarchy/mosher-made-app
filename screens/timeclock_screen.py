import os
import json

from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton,MDButtonText
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ListProperty, DictProperty, StringProperty, ObjectProperty
from kivymd.uix.pickers import MDTimePickerInput, MDModalInputDatePicker
from kivymd.app import MDApp
from kivy.clock import Clock
from data import CheckItem



class TimeClockScreen(MDScreen):
    clocked_in_employees = DictProperty()

    employees = ListProperty()
    check_items = ListProperty()
    
    employers = ListProperty()
    employers_cbs = ObjectProperty()
    employers_boxes = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    def on_pre_enter(self):
        Clock.schedule_once(self.setup_ui)
        
        
    def setup_ui(self, dt=None):
        self.get_currently_clocked_in()
        try:
            self.employees = self.app.rc.employees
            self.employers = self.app.rc.employers
        except Exception as e:
            print(e)
        #self.update_employees()
        #self.update_employers()
    

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
    
    
    def on_employers(self, instance, value):
        print("in on_employers()")
        """Triggered automatically when the bound list updates."""
        self.update_employers()


    def update_employees(self):
        self.ids.check_items_container.clear_widgets()
        self.check_items.clear()
        
        if not self.employees:
            print("No employees to display.")
            check_item = CheckItem(text="No employees found")
            self.ids.check_items_container.add_widget(check_item)
            #self.check_items.append(check_item)
            return

        for employee in self.employees:
            check_item = CheckItem(text=employee)
            if employee in self.clocked_in_employees.keys():
                check_item.checkbox.active = True
            self.ids.check_items_container.add_widget(check_item)
            self.check_items.append(check_item)


    def update_employers(self):
        print(f"Employers found: {self.employers}")
        for emp in self.employers:
            print(emp)
            ecb = CheckItem(text = emp, group = "employer")
            self.employers_cbs.add_widget(ecb)
            self.employers_boxes.append(ecb)


    def get_selected_employer(self):
        for item in self.employers_boxes:
            if item.checkbox.active:
                return item.name_text
        return "No Employer"


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

        print(f"Clocking in: {selected} at {now}")
        self.update_employees()


    def handle_clock_out(self):
        """Example trigger method to be called from a button in your KV file."""
        if self.get_selected_employer() == "No Employer":
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
                    employer_name=self.get_selected_employer(), 
                    time_in=clock_in_time, 
                    time_out=clock_out_time
                )
                del self.clocked_in_employees[employee]
    
        # Update the file after removing employees
        with open("clocked_in.json", "w") as f:
            json.dump(dict(self.clocked_in_employees), f)    
        self.employers_cbs.clear_widgets()
        print(f"Clocking out: {selected}")
        self.update_employees()
        self.update_employers()


#   --- App Properties ---

    @property
    def app(self):
        return MDApp.get_running_app()