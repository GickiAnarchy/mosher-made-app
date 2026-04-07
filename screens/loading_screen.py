from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty
from data import SpinningLogo


class LoadingScreen(MDScreen):
    logo = ObjectProperty()
    
    def on_enter(self):
        self.logo.spin()