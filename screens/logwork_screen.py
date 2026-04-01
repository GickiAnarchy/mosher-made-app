from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from data.dropdownmenu_helper import DropdownMenuHelper

class LogWorkScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Assuming you've initialized your managers elsewhere
        self.menu_helper = DropdownMenuHelper(self, self.app.emp_manager, self.app.job_manager)

    def open_employee_dropdown(self, caller):
        self.menu_helper.create_employee_menu(caller, self.set_employee)

    def open_employer_dropdown(self, caller):
        self.menu_helper.create_employer_menu(caller, self.set_employer)

    def set_employee(self, text_item):
        self.ids.employee_field.text = text_item
        self.menu_helper.employee_menu.dismiss()

    def set_employer(self, text_item):
        self.ids.employer_field.text = text_item
        self.menu_helper.employer_menu.dismiss()

    @property
    def app(self):
        return MDApp.get_running_app()