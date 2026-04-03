
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel

class LogWorkScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.employee_menu = None
        self.employer_menu = None
        self.ids.employee_button.md_bg_color = "#0A279D"  # Blue
        self.ids.employer_button.md_bg_color = "#EBD91B"  # Yellow
        
    
    def open_employee_menu(self, caller):
        # Fetching names from your EmployeeManager
        names = self.manager.timesheet_manager.get_employees()
        print(type(names))
        
        menu_items = [
            {
                "text": f"{name}",
                "on_release": lambda x=name: self.set_employee(x),
            } for name in names
        ]

        self.employee_menu = MDDropdownMenu(
            caller = self.ids.employee_button, items = menu_items
        )
        
        self.employee_menu.open()


    def set_employee(self, employee_name):
        print(f"Selected employee: {employee_name}")
        self.ids.employee_label.text = f"Employee: {employee_name}"
        self.employee_menu.dismiss()


    def open_employer_menu(self, caller):
        # Fetching names from your EmployerManager
        names = self.app.timesheet_manager.get_employers()
        
        menu_items = [
            {
                "text": f"{name}",
                "on_release": lambda x=name: self.set_employer(x),
            } for name in names
        ]
        
        self.employer_menu = MDDropdownMenu(
            caller=self.ids.employer_button,
            items=menu_items,
        )

        self.employer_menu.open()


    def set_employer(self, employer_name):
        print(f"Selected employer: {employer_name}")
        self.ids.employer_label.text = f"Employer: {employer_name}"
        self.employer_menu.dismiss()
