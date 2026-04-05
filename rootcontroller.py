from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarTitle, MDActionTopAppBarButton, MDTopAppBarLeadingButtonContainer
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from data import TimesheetManager, EmployeeManager, EmployerManager
from screens import SCREENS


class RootController(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    toolbar = ObjectProperty()

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.time_manager = TimesheetManager()


    def goto(self, screen_name):
        self.screen_manager.current = screen_name
        self.toolbar.title = screen_name.replace("_", " ").title()
        if self.nav_drawer:
            self.nav_drawer.set_state("closed")


#   --- App Properties ---

    @property
    def app(self):
        return MDApp().get_running_app()
