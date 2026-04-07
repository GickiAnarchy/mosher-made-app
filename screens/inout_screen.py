from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton,MDButtonText
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ListProperty
from kivymd.app import MDApp
from data import CheckItem



class InOutScreen(MDScreen):
    employees = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.check_items = []
        

    def on_enter(self):
        try:
            self.employees = MDApp.get_running_app().rc.employees
        except Exception as e:
            print(e)
                
        self.update_employees()
    

    def on_employees(self, instance, value):
        """Triggered automatically when the bound list updates."""
        self.update_employees()

    def update_employees(self):
        self.ids.check_items_container.clear_widgets()
        self.check_items = []
        
        if not self.employees:
            print("No employees to display.")
            check_item = CheckItem(text="No employees found", group="None")
            self.ids.check_items_container.add_widget(check_item)
            self.check_items.append(check_item)
            return

        for employee in self.employees:
            check_item = CheckItem(text=employee, group="employee")
            self.ids.check_items_container.add_widget(check_item)
            self.check_items.append(check_item)
