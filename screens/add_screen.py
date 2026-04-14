from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

class AddScreen(MDScreen):
    
    def save_employee(self):
        name = self.ids.emp_name_field.text.strip()
        wage = self.ids.emp_wage_field.text.strip()
        
        if name and wage:
            # Send to Google Sheets
            success = self.app.rc.time_manager.add_new_employee(name, wage)
            if success:
                # Reset fields
                self.ids.emp_name_field.text = ""
                self.ids.emp_wage_field.text = ""
                # Refresh global lists so they appear in Clock screen
                self.app.rc.get_lists()
        else:
            print("Please fill out both name and wage.")

    def save_employer(self):
        name = self.ids.employer_name_field.text.strip()
        location = self.ids.employer_loc_field.text.strip()
        
        if name:
            # Send to Google Sheets
            success = self.app.rc.time_manager.add_new_employer(name, location)
            if success:
                self.ids.employer_name_field.text = ""
                self.ids.employer_loc_field.text = ""
                self.app.rc.get_lists()
        else:
            print("Please enter an employer name.")

    @property
    def app(self):
        return MDApp.get_running_app()
