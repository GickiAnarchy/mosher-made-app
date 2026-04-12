import threading
import json
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton,MDButtonText
from kivymd.uix.progressindicator import MDLinearProgressIndicator
from kivy.properties import ObjectProperty, NumericProperty
from kivy.clock import Clock
from data import SpinningLogo



00
class LoadingScreen(MDScreen):
    logo = ObjectProperty()


    def on_pre_enter(self):
        Clock.schedule_once(self.logo.spin)


    def on_enter(self):
        self.try_verify()


    def try_verify(self):
        def vsa():            
            with open("creds.json", "r") as f:
                info = json.load(f)
            if self.app.rc.verify_service_account(info, is_test=False):
                print("service account credentials are valid")
            else:
                print("service account credentials are invalid")
        threading.Thread(target=vsa, daemon=True).start()
        
        
    def try_again(self):
        self.try_verify()


    @property
    def app(self):
        return MDApp.get_running_app()

