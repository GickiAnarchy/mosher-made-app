from screens import SCREENS
from kivymd.app import MDApp
from kivymd.uix.screenmanager import Clock, MDScreenManager
from kivy.properties import ListProperty



class RootScreenManager(MDScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scrn_names = []
        self.build_root()


    def build_root(self):
        for cls, name in SCREENS:
            self.add_widget(cls(name = name))
            self.scrn_names.append(name)
            print(f"screen {name} added")
        self.goto("loading")


    def goto(self, screen_name):
        if screen_name not in self.scrn_names:
            print(f"{screen_name} not a screen name")
            return
        print(f"going to {screen_name}")
        self.current = screen_name        
    

    @property
    def rc(self):
        return self.app.rc


    @property
    def app(self):
        return MDApp.get_running_app()