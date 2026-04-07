from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarTitle, MDActionTopAppBarButton, MDTopAppBarLeadingButtonContainer
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationDrawerItem, MDNavigationDrawerItemText, MDNavigationDrawerItemLeadingIcon
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
        self.time_manager = None

        Clock.schedule_once(self.get_lists,1)
        


    def get_lists(self, dt = None):
        self.time_manager = TimesheetManager()
        self.employees = self.time_manager.get_employees()
        self.employers = self.time_manager.get_employers()
        self.screen_manager.current = "home"


    def on_employees(self, instance, value):
        print("Employee list changed")


    def on_employers(self, instance, value):
        print("Employer list changed")


    def goto(self, screen_name):
        try:
            self.screen_manager.current = screen_name
        except Exception as e:
            print(e)
            return
        
        # In KivyMD 2.0, we find the MDTopAppBarTitle child to update the title
        for child in self.toolbar.children:
            if isinstance(child, MDTopAppBarTitle):
                child.text = screen_name.replace("_", " ").title()
                break

        if self.nav_drawer:
            self.nav_drawer.set_state("closed")

#   --- App Properties ---

    @property
    def app(self):
        return MDApp.get_running_app()
