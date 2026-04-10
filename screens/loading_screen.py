from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from data import SpinningLogo


class LoadingScreen(MDScreen):
    logo = ObjectProperty()


    def on_pre_enter(self):
        Clock.schedule_once(self.logo.spin,0)


    def on_enter(self):
        self.app.rc.verify_creds()
        print(self.app.rc.valid_key)
        if self.app.rc.valid_key:
            self.app.rc.get_lists()
        else:
            self.app.rc.screen_manager.current = "needkey"


    @property
    def app(self):
        return MDApp.get_running_app()