import os
import json

from kivymd.material_resources import dp

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, MDListItem
from kivymd.uix.navigationrail import MDNavigationRailItem,MDNavigationRail,MDNavigationRailMenuButton,MDNavigationRailFabButton,MDNavigationRailItemIcon,MDNavigationRailItemLabel

from kivy.clock import Clock

from rootcontroller import RootController
from screens import SCREENS
from data import verify_service_account


class MosherMadeApp(MDApp):
    def __init__(self, **kwargs):
        print("init - before super")
        super().__init__(**kwargs)
        self.key_is_valid = False
        print("init - after super")


    def build(self):
        print("build called")
        self.rc = RootController()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return self.rc


    def on_start(self):
        self.fps_monitor_start()
        