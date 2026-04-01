from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import DDropdownMenu
from kivymd.uix.list import MDListItem, MDListItemHeadlineText
from kivymd.app import MDApp

class LogWorkScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.employee_menu = None
        self.employer_menu = None

    def open_employee_menu(self, caller):
        # Access managers through the main App instance
        app = MDApp.get_running_app()
        names = app.employee_manager.get_names()
        
        menu_items = [
            MDListItem(
                MDListItemHeadlineText(text=name),
                on_release=lambda x=name: self.set_employee(x),
            ) for name in names
        ]
        
        self.employee_menu = MDMenu(caller=caller, items=menu_items)
        self.employee_menu.open()

    def set_employee(self, name):
        self.ids.employee_field.text = name
        self.employee_menu.dismiss()

    def open_employer_menu(self, caller):
        app = MDApp.get_running_app()
        names = app.employer_manager.get_names()
        
        menu_items = [
            MDListItem(
                MDListItemHeadlineText(text=name),
                on_release=lambda x=name: self.set_employer(x),
            ) for name in names
        ]
        
        self.employer_menu = MDMenu(caller=caller, items=menu_items)
        self.employer_menu.open()

    def set_employer(self, name):
        self.ids.employer_field.text = name
        self.employer_menu.dismiss()
