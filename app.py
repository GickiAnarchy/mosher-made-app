from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, MDListItem

from data import DropdownMenuHelper, EmployeeManager, EmployerManager, TimesheetManager, get_log_and_data_worksheets
from screens.logwork_screen import LogWorkScreen




class MosherMadeApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data_ws, log_ws = get_log_and_data_worksheets()
        self.employee_manager = EmployeeManager(data_ws)
        self.employer_manager = EmployerManager(data_ws)
        self.timesheet_manager = TimesheetManager(log_ws, self.employee_manager, self.employer_manager)


    def build(self):
        self.screen_manager = MDScreenManager()
        self.screen_manager.add_widget(LogWorkScreen(name="logwork"))
        return self.screen_manager