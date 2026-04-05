from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarTitle, MDActionTopAppBarButton, MDTopAppBarLeadingButtonContainer
from kivy.properties import ObjectProperty, ListProperty
from kivy.clock import Clock

from data import TimesheetManager, EmployeeManager, EmployerManager
from screens import SCREENS


class RootController(MDBoxLayout):
    # WIDGETS
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    toolbar = ObjectProperty()

    # DATA
    employees = ListProperty([])
    employers = ListProperty([])

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.time_manager = TimesheetManager()

        Clock.schedule_once(self.get_lists,1)


    def get_lists(self, dt = None):
        self.employees = TimesheetManager.get_employees()
        self.employers = TimesheetManager.get_employers()


    def on_employees(self, instance, value):
        super().on_enter(instance, value)
        print("Employee list changed")


    def on_employers(self, instance, value):
        super().on_enter(instance, value)
        print("Employer list changed")


    def goto(self, screen_name):
        self.screen_manager.current = screen_name
        self.toolbar.title = screen_name.replace("_", " ").title()
        if self.nav_drawer:
            self.nav_drawer.set_state("closed")


#   --- App Properties ---

    @property
    def app(self):
        return MDApp().get_running_app()
