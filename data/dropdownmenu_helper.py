from kivymd.uix.menu import MDDropdownMenu

class DropdownMenuHelper:
    def __init__(self, screen, employee_manager, employer_manager):
        self.screen = screen
        self.emp_manager = employee_manager
        self.job_manager = employer_manager
        
        # Menu instances
        self.employee_menu = None
        self.employer_menu = None


    def create_employee_menu(self, caller, on_select_callback):
        """
        caller: The UI element (like a button or textfield) the menu attaches to.
        on_select_callback: A function to run when an item is clicked.
        """
        # Fetch fresh names from your EmployeeManager
        names = self.emp_manager.get_names()
        
        menu_items = [
            {
                "text": name,
                "on_release": lambda x=name: on_select_callback(x),
            } for name in names
        ]
        
        self.employee_menu = MDDropdownMenu(
            caller=caller,
            items=menu_items,
        )
        self.employee_menu.open()


    def create_employer_menu(self, caller, on_select_callback):
        """Fetch names from EmployerManager and open menu."""
        names = self.job_manager.get_names()
        
        menu_items = [
            {
                "text": name,
                "on_release": lambda x=name: on_select_callback(x),
            } for name in names
        ]
        
        self.employer_menu = MDDropdownMenu(
            caller=caller,
            items=menu_items,
        )
        self.employer_menu.open()
