from screens import SCREENS
from kivymd.app import MDApp
from kivymd.uix.screenmanager import Clock, MDScreenManager
from kivy.properties import ListProperty



class RootScreenManager(MDScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_names = []    


    def build_root(self):
        

    
    def goto(self, screen_name):
        if screen_name not in self.screen_names:
            print(f"{screen_name} not a screen name")
            return
        self.current = screen_name

    @property
    def app(self):
        return MDApp.get_running_app()