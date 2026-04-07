import threading
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
        
        self.nav_drawer.disabled = True
        self.toolbar.disabled = True
        

    def get_lists(self, dt = None):
        def fetch_data():
            # Blocking network calls happen in this background thread
            tm = TimesheetManager()
            employees = tm.get_employees()
            employers = tm.get_employers()
            
            # Schedule UI updates back on the main thread
            Clock.schedule_once(lambda x: self._finalize_data(tm, employees, employers))

        threading.Thread(target=fetch_data, daemon=True).start()


    def _finalize_data(self, tm, employees, employers):
        self.time_manager = tm
        self.employees = employees
        self.employers = employers
        print(f"Employers: {self.employers}")
        self.nav_drawer.disabled = False
        self.toolbar.disabled = False
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
        self.toolbar.title = screen_name.replace("_"," ").title()
        if self.nav_drawer:
            self.nav_drawer.set_state("closed")

#   --- App Properties ---

    @property
    def app(self):
        return MDApp.get_running_app()