from screens import SCREENS
from kivymd.app import MDApp
from kivymd.uix.screenmanager import Clock, MDScreenManager
from kivy.properties import ListProperty



class RootController(MDScreenManager):
    employee_list = ListProperty([])
    employer_list = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timesheet_manager = None
    
    
    def build_root(self, tm):
        self.timesheet_manager = tm
        Clock.schedule_once(self.get_lists, 0.5)  # Delay to ensure everything is initialized
        
        for cls, name in SCREENS:
            self.add_widget(cls(name=name))
            print(f"Added screen: {name}")
        self.current = "home"


    def get_lists(self, dt):
        print("Fetching employee and employer lists...")
        self.employee_list = self.timesheet_manager.get_employees()
        self.employer_list = self.timesheet_manager.get_employers()
        print("Retrieved Lists")





    @property
    def app(self):
        return MDApp.get_running_app()