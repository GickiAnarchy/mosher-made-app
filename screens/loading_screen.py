import threading
import json
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton,MDButtonText
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from data import SpinningLogo


class LoadingScreen(MDScreen):
    logo = ObjectProperty()


    def on_pre_enter(self):
        Clock.schedule_once(self.logo.spin,0)


    def on_enter(self):
        print("loading_screen.on_enter()")
        self.try_verify()
    

    def try_verify(self):
        def vsa():
            with open("creds.json","r") as f:
                info = json.load(f)
            self.app.rc.verify_service_account(info, is_test = False)
        threading.Thread(target=vsa, daemon=True).start()


    def try_again(self):
        self.try_verify()


    @property
    def app(self):
        return MDApp.get_running_app()

