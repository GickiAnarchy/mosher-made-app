from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.list import MDListItem, MDListItemHeadlineText

class AddScreen(MDScreen):
    editing_employee_name = StringProperty("")
    editing_employer_name = StringProperty("")

    def on_pre_enter(self, *args):
        """Called before the screen is displayed. Refreshes lists."""
        self.refresh_employee_list()
        self.refresh_employer_list()

    def refresh_employee_list(self):
        """Clears and repopulates the employee list."""
        if 'employee_list' not in self.ids:
            return
        container = self.ids.employee_list
        container.clear_widgets()
        
        for name in self.app.rc.employees:
            item = MDListItem(
                MDListItemHeadlineText(text=name),
                on_release=lambda x, n=name: self.select_employee(n)
            )
            container.add_widget(item)

    def select_employee(self, name):
        """Sets the selected employee and fills input fields."""
        self.editing_employee_name = name
        emp_data = self.app.rc.time_manager.employee_manager.get(name)
        if emp_data:
            self.ids.emp_name_field.text = emp_data.get('name', '')
            self.ids.emp_wage_field.text = emp_data.get('wage', '')

    def refresh_employer_list(self):
        """Clears and repopulates the employer list."""
        if 'employer_list' not in self.ids:
            return
        container = self.ids.employer_list
        container.clear_widgets()
        for name in self.app.rc.employers:
            item = MDListItem(
                MDListItemHeadlineText(text=name),
                on_release=lambda x, n=name: self.select_employer(n)
            )
            container.add_widget(item)

    def select_employer(self, name):
        """Sets the selected employer and fills input fields."""
        self.editing_employer_name = name
        emp_data = self.app.rc.time_manager.employer_manager.get(name)
        if emp_data:
            self.ids.employer_name_field.text = emp_data.get('name', '')
            self.ids.employer_loc_field.text = emp_data.get('location', '')
    
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

    def update_employee(self, old_name=None):
        if not old_name:
            old_name = self.editing_employee_name
        name = self.ids.emp_name_field.text.strip()
        wage = self.ids.emp_wage_field.text.strip()
        if old_name and (name or wage):
            self.app.rc.time_manager.update_employee(old_name, name, wage)
            self.ids.emp_name_field.text = ""
            self.ids.emp_wage_field.text = ""
            self.editing_employee_name = ""
            self.app.rc.get_lists()
            self.refresh_employee_list()

    def delete_employee(self, name=None):
        if not name:
            name = self.editing_employee_name or self.ids.emp_name_field.text.strip()
        if name:
            self.app.rc.time_manager.delete_employee(name)
            self.ids.emp_name_field.text = ""
            self.editing_employee_name = ""
            self.app.rc.get_lists()
            self.refresh_employee_list()

    def update_employer(self, old_name=None):
        if not old_name:
            old_name = self.editing_employer_name
        name = self.ids.employer_name_field.text.strip()
        location = self.ids.employer_loc_field.text.strip()
        if old_name and (name or location):
            self.app.rc.time_manager.update_employer(old_name, name, location)
            self.ids.employer_name_field.text = ""
            self.ids.employer_loc_field.text = ""
            self.editing_employer_name = ""
            self.app.rc.get_lists()
            self.refresh_employer_list()

    def delete_employer(self, name=None):
        if not name:
            name = self.editing_employer_name or self.ids.employer_name_field.text.strip()
        if name:
            self.app.rc.time_manager.delete_employer(name)
            self.ids.employer_name_field.text = ""
            self.editing_employer_name = ""
            self.app.rc.get_lists()
            self.refresh_employer_list()

    @property
    def app(self):
        return MDApp.get_running_app()
