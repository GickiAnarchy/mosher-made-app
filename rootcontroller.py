import threading
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.auth.exceptions import DefaultCredentialsError

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarTitle, MDActionTopAppBarButton, MDTopAppBarLeadingButtonContainer
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationDrawerItem, MDNavigationDrawerItemText, MDNavigationDrawerItemLeadingIcon
from kivy.properties import ObjectProperty, ListProperty, BooleanProperty
from kivy.clock import Clock
Clock.max_iteration = 20
from data import TimesheetManager
from rootscreenmanager import RootScreenManager


class RootController(MDBoxLayout):
    # WIDGETS
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    toolbar = ObjectProperty()
    toolbar_title = ObjectProperty()

    # DATA
    valid_key = BooleanProperty()
    employees = ListProperty([])
    employers = ListProperty([])

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.time_manager = None
        self.nav_drawer.disabled = True
        self.toolbar.disabled = True
        self.valid_key = False

        
    def on_enter(self):
        pass
        #self.screen_manager.build_root()


    def get_lists(self):
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
        self.ids.toolbar_title.text = screen_name.replace("_"," ").title()
        if self.nav_drawer:
            self.nav_drawer.set_state("closed")



#   --- Credentials Management ---

    def verify_service_account(self, info, is_test = True):
        """
        Verifies Google Service Account credentials.
        'info' can be a dictionary or a JSON string.
        If None, it attempts to load from the default local file.
        """
        print("verify_service_account called")
        try:
            # 1. Attempt to create credentials object
            creds = service_account.Credentials.from_service_account_info(info)
            # 2. Scope the credentials (e.g., for Google Drive or Cloud Storage)
            # Even if you don't use the API, scoping is required to verify
            scoped_creds = creds.with_scopes(['https://www.googleapis.com/auth/cloud-platform'])
            # 3. Build a service and make a 'test' call
            # We use the Service Usage API to see if we can at least authenticate
            service = build('serviceusage', 'v1', credentials=scoped_creds)
            
            # This triggers a refresh/validation check
            print(f"Success! Authenticated as: {creds.service_account_email}")
            if is_test is False:
                self.valid_key = True
            return True
        except Exception as e:
            print(f"Verification Failed: {e}")
            return False


    def on_valid_key(self, instance, value):
        if value is True:
            print("Credentials are valid.")
            self.get_lists()
        else:
            print("Credentials are invalid.")


#   --- App Properties ---

    @property
    def app(self):
        return MDApp.get_running_app()
    