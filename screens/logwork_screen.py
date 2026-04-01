# from kivy.factory import Factory
# from kivymd.uix.list import OneLineListItem
# Factory.register('OneLineListItem', cls=OneLineListItem)

from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivymd.uix.list import MDListItem, MDListItemHeadlineText

class LogWorkScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.employee_menu = None
        self.employer_menu = None

    def open_employee_menu(self, caller):
        app = MDApp.get_running_app()
        # Fetching names from your EmployeeManager
        names = app.employee_manager.get_names()
        
        # FIX: The menu needs a list of DICTIONARIES, not MDListItem widgets
        menu_items = [
            {
                "viewclass": "MDListItemHeadlineText",
                "text": name,
                "on_release": lambda x=name: self.set_employee(x),
                "on_selected": lambda x=name: self.set_employee(x),
            } for name in names
        ]
        
        self.employee_menu = MDDropdownMenu(
            caller=caller, 
            items=menu_items,
            width_mult=4
        )
        self.employee_menu.open()

    def set_employee(self, selected_item):
        print(f"Selected employee: {selected_item.text}")
        # selected_item is the widget instance created by the menu
        self.ids.employee_field.text = selected_item.text
        self.employee_menu.dismiss()

    def open_employer_menu(self, caller):
        app = MDApp.get_running_app()
        # Fetching names from your EmployerManager
        names = app.employer_manager.get_names()
        
        menu_items = [
            {
                "viewclass": "MDListItemHeadlineText",
                "text": name,
                "on_release": lambda x=name: self.set_employer(x),
                "on_selected": lambda x=name: self.set_employer(x),
            } for name in names
        ]
        
        self.employer_menu = MDDropdownMenu(
            caller=caller, 
            items=menu_items,
            width_mult=4
        )
        self.employer_menu.open()

    def set_employer(self, selected_item):
        print(f"Selected employer: {selected_item.text}")
        self.ids.employer_field.text = selected_item.text
        self.employer_menu.dismiss()