from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton,MDButtonText
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from data import CheckItem



class InOutScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.check_items = []
        self.employees = None
        self.employers = None


    def on_enter(self):
        self.employees = self.manager.employee_list
        self.employers = self.manager.employer_list
        self.populate_check_items()
    

    def populate_check_items(self):
        self.ids.check_items_container.clear_widgets()
        self.check_items = []
        
        for employee in self.employees:
            check_item = CheckItem(text=employee, group="employee")
            self.ids.check_items_container.add_widget(check_item)
            self.check_items.append(check_item)
