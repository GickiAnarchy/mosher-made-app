
import os
import json

from kivymd.uix.dialog import MDDialog,MDDialogContentContainer,MDDialogButtonContainer
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage
from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarTitle
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationDrawerItem
from kivymd.uix.screenmanager import MDScreenManager
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, DictProperty
from kivy.clock import Clock




SAVE_FILE = "data/saved.json"


class RootController(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    topbar = ObjectProperty()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = {}
        Clock.schedule_once(self.setup_screens, 1)
        Clock.schedule_once(self.setup_data, 1.5)


##    SCREEN MANAGEMENT
    def setup_screens(self,dt):
        from screens import SCREENS
        for cls,name in SCREENS:
            self.screen_manager.add_widget(cls(name=name))
        
        self.screen_manager.current = "home"


    def goto(self, screenName):
        self.screen_manager.current = screenName
        for child in self.topbar.children:
            if isinstance(child, MDTopAppBarTitle):
                child.text = screenName.replace("_", " ").title()
        if self.nav_drawer:
            self.nav_drawer.set_state("close")


##    DATA MANAGEMENT
    def load_data(self):
        if not os.path.exists(SAVE_FILE):
            return {}
        try:
            with open(SAVE_FILE,"r") as f:
                data = json.load(f)
        except Exception as e:
            print(f"E R R O R\n{e}")
        return data


    def save_data(self, newData):
        try:
            with open(SAVE_FILE,"w") as f:
                json.dump(newData,f,indent=4)
        except Exception as e:
            print(f"E R R O R\n{e}")
        print("Data saved")

    def setup_data(self,dt):
        self.data = self.load_data()
        self.employees = self.data.get("employees",[])
        self.employers = self.data.get("employers",[])

