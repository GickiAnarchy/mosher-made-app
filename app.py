from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, MDListItem

from kivy.clock import Clock

from data import DropdownMenuHelper, EmployeeManager, EmployerManager, TimesheetManager, get_log_and_data_worksheets
from screens.logwork_screen import LogWorkScreen




class MosherMadeApp(MDApp):
    def __init__(self, **kwargs):
        print("init - before super")
        super().__init__(**kwargs)
        print("init - after super")
        self.data_ws = None
        self.log_ws = None
        self.get_worksheets()
        #Clock.schedule_once(self.get_worksheets, 0)


    def build(self):
        print("build called")
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"

        self.screen_manager = MDScreenManager()
        Clock.schedule_once(self.populate_screens, 1)
        return self.screen_manager


    def populate_screens(self, dt):
        self.screen_manager.add_widget(LogWorkScreen(name="logwork"))


    def get_worksheets(self, dt=None):
        self.data_ws, self.log_ws = get_log_and_data_worksheets()
        self.timesheet_manager = TimesheetManager(self.log_ws, self.data_ws)