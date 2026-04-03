from screens import SCREENS
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager



class RootController(MDScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timesheet_manager = None
    
    
    def build_root(self, tm):
        self.timesheet_manager = tm
        
        for cls, name in SCREENS:
            self.add_widget(cls(name=name))
            print(f"Added screen: {name}")


    def clock_in(self, employees, employer):
        pass


    def clock_out(self, employees, employer):
        pass
    
    
    @property
    def app(self):
        return MDApp.get_running_app()